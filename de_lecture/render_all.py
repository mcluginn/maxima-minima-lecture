import os
import subprocess
import shutil

SCENES = [
    "Scene01_IntroDE",
    "Scene02_ModelingBlueprint",
    "Scene03_SeparationVariables",
    "Scene04_NewtonCoolingLaw",
    "Scene05_CoolingProblem1_Thermometer6Min",
    "Scene06_CoolingProblem2_HalfDegree",
    "Scene07_ChemicalConversion_Decay",
    "Scene08_RadiumProblem1_HalfLife",
    "Scene09_DecayProblem2_90Percent",
    "Scene10_EscapeVelocity",
    "Scene11_SynthesisComparison",
]

OUTPUT_VIDEOS_DIR = os.path.join("public", "videos")
OUTPUT_FRAMES_DIR = os.path.join("public", "frames")
os.makedirs(OUTPUT_VIDEOS_DIR, exist_ok=True)
os.makedirs(OUTPUT_FRAMES_DIR, exist_ok=True)

PYTHON_EXE = os.path.join(".venv", "Scripts", "python.exe")

for idx, scene_name in enumerate(SCENES, 1):
    print(f"\n=======================================================")
    print(f"[{idx}/{len(SCENES)}] Rendering Manim Scene: {scene_name}")
    print(f"=======================================================")

    cmd = [
        PYTHON_EXE, "-m", "manim",
        "-qm",
        os.path.join("de_lecture", "render_de_scenes.py"),
        scene_name
    ]

    ret = subprocess.run(cmd)
    if ret.returncode != 0:
        print(f"ERROR: Failed rendering {scene_name}")
        continue

    # Path to generated MP4
    src_mp4 = os.path.join("media", "videos", "render_de_scenes", "720p30", f"{scene_name}.mp4")
    dst_mp4 = os.path.join(OUTPUT_VIDEOS_DIR, f"{scene_name}.mp4")
    dst_png = os.path.join(OUTPUT_FRAMES_DIR, f"{scene_name}.png")

    if os.path.exists(src_mp4):
        shutil.copy2(src_mp4, dst_mp4)
        print(f"Copied MP4 to: {dst_mp4}")

        # Extract last frame as high-res PNG
        ffmpeg_cmd = [
            "ffmpeg", "-sseof", "-0.5", "-i", dst_mp4,
            "-update", "1", "-q:v", "2", dst_png, "-y"
        ]
        subprocess.run(ffmpeg_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"Extracted still frame to: {dst_png}")
    else:
        print(f"Warning: Expected output not found at {src_mp4}")

print("\nAll scenes processed successfully!")
