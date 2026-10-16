import os
import subprocess
import shutil
import sys

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
PYTHON_EXE = os.path.join(ROOT_DIR, ".venv", "Scripts", "python.exe")
FFMPEG_EXE = r"C:\ffmpeg-8.1-full_build\bin\ffmpeg.exe"

CLIPS_DIR = os.path.join(ROOT_DIR, "media", "videos", "clips")
PUBLIC_CLIPS_DIR = os.path.join(ROOT_DIR, "public", "media", "videos", "clips")
FRAMES_DIR = os.path.join(ROOT_DIR, "media", "frames")
PUBLIC_FRAMES_DIR = os.path.join(ROOT_DIR, "public", "media", "frames")

os.makedirs(CLIPS_DIR, exist_ok=True)
os.makedirs(PUBLIC_CLIPS_DIR, exist_ok=True)
os.makedirs(FRAMES_DIR, exist_ok=True)
os.makedirs(PUBLIC_FRAMES_DIR, exist_ok=True)

MATHALINO_SCENES = [
    "MathalinoProblem1_NumberOptimization",
    "MathalinoProblem2_RiverbankLot",
    "MathalinoProblem3_OpenTopBox",
    "MathalinoProblem4_TourBusRevenue",
    "MathalinoProblem5_TrapezoidalGutter",
]

def render_and_export(scene_name):
    print(f"\n{'='*60}\nRendering Mathalino Scene: {scene_name}\n{'='*60}")
    script_path = os.path.join(ROOT_DIR, "manim_lecture", "mathalino_problems.py")
    cmd = [PYTHON_EXE, "-m", "manim", "-qh", script_path, scene_name]
    
    res = subprocess.run(cmd, cwd=ROOT_DIR)
    if res.returncode != 0:
        print(f"FAILED rendering {scene_name} (code: {res.returncode})")
        return False
        
    src_mp4 = os.path.join(ROOT_DIR, "media", "videos", "mathalino_problems", "1080p30", f"{scene_name}.mp4")
    if not os.path.exists(src_mp4):
        print(f"Error: expected output MP4 not found at {src_mp4}")
        return False
        
    # Copy to clips directories
    dst_clip1 = os.path.join(CLIPS_DIR, f"{scene_name}.mp4")
    dst_clip2 = os.path.join(PUBLIC_CLIPS_DIR, f"{scene_name}.mp4")
    shutil.copy2(src_mp4, dst_clip1)
    shutil.copy2(src_mp4, dst_clip2)
    print(f"Copied MP4 to clips: {dst_clip1}")
    
    # Extract still frame
    dst_frame1 = os.path.join(FRAMES_DIR, f"{scene_name}_frame.png")
    dst_frame2 = os.path.join(PUBLIC_FRAMES_DIR, f"{scene_name}_frame.png")
    ffmpeg_cmd = [
        FFMPEG_EXE, "-sseof", "-0.1", "-i", src_mp4,
        "-update", "1", "-q:v", "1", dst_frame1, "-y"
    ]
    subprocess.run(ffmpeg_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    shutil.copy2(dst_frame1, dst_frame2)
    print(f"Extracted still frame: {dst_frame1}")
    return True

def main():
    print(f"Starting render of {len(MATHALINO_SCENES)} Mathalino Scenes...")
    success = []
    for s in MATHALINO_SCENES:
        if render_and_export(s):
            success.append(s)
        else:
            print(f"ABORTING due to error in {s}")
            break
            
    print(f"\nRender completed: {len(success)}/{len(MATHALINO_SCENES)} scenes rendered successfully.")

if __name__ == "__main__":
    main()
