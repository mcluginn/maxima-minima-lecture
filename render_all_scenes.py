import os
import subprocess
import sys
import glob

# Paths
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
PYTHON_EXE = os.path.join(ROOT_DIR, ".venv", "Scripts", "python.exe")
FFMPEG_EXE = r"C:\ffmpeg-8.1-full_build\bin\ffmpeg.exe"
OUTPUT_DIR = os.path.join(ROOT_DIR, "media", "videos")
FRAMES_DIR = os.path.join(ROOT_DIR, "media", "frames")

os.makedirs(FRAMES_DIR, exist_ok=True)

# List of all scenes to render
SCENES = [
    # Signature 7-Scene Sequence
    ("manim_lecture/signature_sequence.py", "SignatureScene1_TheFunction"),
    ("manim_lecture/signature_sequence.py", "SignatureScene2_TheTangent"),
    ("manim_lecture/signature_sequence.py", "SignatureScene3_EquationMorph"),
    ("manim_lecture/signature_sequence.py", "SignatureScene4_DerivativeTest"),
    ("manim_lecture/signature_sequence.py", "SignatureScene5_ExtremaReveal"),
    ("manim_lecture/signature_sequence.py", "SignatureScene6_SecondDerivative"),
    ("manim_lecture/signature_sequence.py", "SignatureScene7_Counterexample"),
    # Broader Curriculum Scenes
    ("manim_lecture/broader_scenes.py", "Scene01_HookHill"),
    ("manim_lecture/broader_scenes.py", "Scene02_LocalVsAbsolute"),
    ("manim_lecture/broader_scenes.py", "Scene03_SingularitiesDNE"),
    ("manim_lecture/broader_scenes.py", "Scene04_ClosedIntervalMethod"),
    ("manim_lecture/broader_scenes.py", "Scene05_MaxPowerTransfer"),
]

def render_scene(script_rel_path, scene_name, quality="-qm"):
    script_path = os.path.join(ROOT_DIR, script_rel_path)
    cmd = [PYTHON_EXE, "-m", "manim", quality, script_path, scene_name]
    print(f"\n=======================================================")
    print(f"RENDERING: {scene_name} from {script_rel_path}")
    print(f"COMMAND: {' '.join(cmd)}")
    print(f"=======================================================")
    res = subprocess.run(cmd, cwd=ROOT_DIR)
    if res.returncode != 0:
        print(f"ERROR rendering {scene_name}! Exit code: {res.returncode}")
        return False
    return True

def extract_frame(scene_name):
    # Locate rendered MP4
    search_pattern = os.path.join(ROOT_DIR, "media", "videos", "**", f"{scene_name}.mp4")
    matching_mp4s = glob.glob(search_pattern, recursive=True)
    if not matching_mp4s:
        print(f"WARNING: Could not find rendered MP4 for {scene_name}")
        return False
    
    mp4_path = matching_mp4s[0]
    out_frame_path = os.path.join(FRAMES_DIR, f"{scene_name}_frame.png")
    
    # FFmpeg extract last frame
    cmd = [
        FFMPEG_EXE, "-sseof", "-0.1", "-i", mp4_path,
        "-update", "1", "-q:v", "1", out_frame_path, "-y"
    ]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"EXTRACTED STILL FRAME: {out_frame_path}")
    return True

def main():
    quality = "-qm" # 720p30 for fast, clean rendering
    if len(sys.argv) > 1:
        quality = sys.argv[1]
    
    print(f"Starting master render of {len(SCENES)} scenes at quality {quality}...")
    success_count = 0
    for script, scene in SCENES:
        out_frame_path = os.path.join(FRAMES_DIR, f"{scene}_frame.png")
        if os.path.exists(out_frame_path) and "--force" not in sys.argv:
            print(f"ALREADY RENDERED: {scene} (frame exists at {out_frame_path})")
            success_count += 1
            continue

        ok = render_scene(script, scene, quality)
        if ok:
            extract_frame(scene)
            success_count += 1
        else:
            print(f"FAILED on scene: {scene}")
            break
            
    print(f"\nRender process complete. Successfully rendered/verified {success_count}/{len(SCENES)} scenes.")

if __name__ == "__main__":
    main()
