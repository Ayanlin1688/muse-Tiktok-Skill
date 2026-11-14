#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Muse Video Studio · 抽帧自查

用法:
  python extract_frames.py <video> [n=3] [--outdir DIR] [--prefix PREFIX]

输出:
  <prefix>-f1.png ... <prefix>-fN.png，逐行打印绝对路径，末行给汇总。
依赖:
  ffmpeg / ffprobe 在 PATH 中。
"""
import argparse
import shutil
import subprocess
import sys
from pathlib import Path

for _s in (sys.stdout, sys.stderr):
    if hasattr(_s, "reconfigure"):
        _s.reconfigure(encoding="utf-8", errors="replace")


def die(msg, code=2):
    print(f"[错误] {msg}", file=sys.stderr)
    sys.exit(code)


def probe_duration(video: Path) -> float:
    r = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", str(video)],
        capture_output=True, text=True,
    )
    if r.returncode != 0:
        die(f"ffprobe 读不到时长: {video}\n{r.stderr.strip()}")
    try:
        return float(r.stdout.strip())
    except ValueError:
        die(f"时长解析失败: {r.stdout!r}")


def main():
    p = argparse.ArgumentParser(description="Muse 视频抽帧自查")
    p.add_argument("video", help="视频文件路径")
    p.add_argument("n", nargs="?", type=int, default=3, help="抽帧数，默认 3")
    p.add_argument("--outdir", default=None, help="输出目录，默认与视频同目录")
    p.add_argument("--prefix", default=None, help="输出前缀，默认视频文件名")
    args = p.parse_args()

    if shutil.which("ffmpeg") is None or shutil.which("ffprobe") is None:
        die("找不到 ffmpeg / ffprobe，请先安装并加入 PATH")
    video = Path(args.video).expanduser().resolve()
    if not video.is_file():
        die(f"视频不存在: {video}")
    if args.n < 1:
        die("抽帧数必须 >= 1")

    outdir = Path(args.outdir).expanduser().resolve() if args.outdir else video.parent
    outdir.mkdir(parents=True, exist_ok=True)
    prefix = args.prefix or video.stem
    dur = probe_duration(video)
    if dur <= 0:
        die(f"视频时长异常: {dur}")

    outs = []
    for i in range(args.n):
        t = dur * (i + 0.5) / args.n
        out = outdir / f"{prefix}-f{i + 1}.png"
        r = subprocess.run(
            ["ffmpeg", "-y", "-loglevel", "error", "-ss", f"{t:.3f}",
             "-i", str(video), "-vframes", "1", str(out)],
            capture_output=True, text=True,
        )
        if r.returncode != 0:
            die(f"抽第 {i + 1} 帧失败 @ {t:.2f}s\n{r.stderr.strip()}")
        print(str(out))
        outs.append(out)

    print(f"\n完成：{len(outs)} 帧，时长 {dur:.2f}s -> {outdir}")


if __name__ == "__main__":
    main()
