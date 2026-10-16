"""
generate_presentation_deck.py
Generates a premium, Keynote-compatible 16:9 widescreen presentation deck (PPTX)
featuring embedded Manim 1080p MP4 clips and matching Apple Pencil annotation slides.
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

# Design Tokens (Midnight Navy Theme)
BG_COLOR = RGBColor(11, 15, 25)       # #0B0F19
CARD_BG = RGBColor(19, 27, 46)        # #131B2E
CARD_BORDER = RGBColor(51, 65, 85)    # #334155
CYAN = RGBColor(56, 189, 248)         # #38BDF8
AMBER = RGBColor(245, 158, 11)        # #F59E0B
CORAL = RGBColor(244, 63, 94)         # #F43F5E
TEXT_WHITE = RGBColor(248, 250, 252)  # #F8FAFC
TEXT_MUTED = RGBColor(148, 163, 184)  # #94A3B8
GREEN = RGBColor(34, 197, 94)         # #22C55E

def create_deck(output_pptx="presentation/maxima_minima_lecture.pptx"):
    os.makedirs(os.path.dirname(output_pptx), exist_ok=True)
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    def set_slide_background(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = BG_COLOR
        bg.line.fill.background()
        return bg

    def add_header(slide, title, category="DIFFERENTIAL CALCULUS // ENGINEERING LECTURE"):
        # Header banner text box
        tb = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.733), Inches(0.9))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        
        p_cat = tf.paragraphs[0]
        p_cat.text = category.upper()
        p_cat.font.size = Pt(11)
        p_cat.font.bold = True
        p_cat.font.color.rgb = CYAN
        
        p_title = tf.add_paragraph()
        p_title.text = title
        p_title.font.size = Pt(24)
        p_title.font.bold = True
        p_title.font.color.rgb = TEXT_WHITE

    def add_card(slide, left, top, width, height, border_color=CARD_BORDER, bg_color=CARD_BG):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = bg_color
        card.line.color.rgb = border_color
        card.line.width = Pt(1.5)
        return card

    # -------------------------------------------------------------
    # SLIDE 1: Title Slide
    # -------------------------------------------------------------
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_background(s1)
    
    # Title Hero Card
    add_card(s1, Inches(1.2), Inches(1.2), Inches(10.933), Inches(5.1), border_color=CYAN)
    tb1 = s1.shapes.add_textbox(Inches(1.8), Inches(1.8), Inches(9.733), Inches(3.9))
    tf1 = tb1.text_frame
    tf1.word_wrap = True
    
    p = tf1.paragraphs[0]
    p.text = "DIFFERENTIAL CALCULUS FOR ENGINEERS"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = CYAN
    
    p2 = tf1.add_paragraph()
    p2.text = "Maxima & Minima: Dynamic Motion, Extrema Tests & Optimization"
    p2.font.size = Pt(36)
    p2.font.bold = True
    p2.font.color.rgb = TEXT_WHITE
    p2.space_before = Pt(14)
    
    p3 = tf1.add_paragraph()
    p3.text = "A Motion-Graphics Interactive Lecture Designed for Live iPad & Apple Pencil Annotation"
    p3.font.size = Pt(18)
    p3.font.color.rgb = AMBER
    p3.space_before = Pt(14)

    p4 = tf1.add_paragraph()
    p4.text = "Core Function: f(x) = x³ - 3x  |  Engineering Application: Maximum Power Transfer"
    p4.font.size = Pt(13)
    p4.font.color.rgb = TEXT_MUTED
    p4.space_before = Pt(24)

    s1.notes_slide.notes_text_frame.text = (
        "OPENING REMARKS:\n"
        "Welcome students. Today we connect the geometry of motion with rigorous calculus.\n"
        "We will discover how derivatives act as velocity detectors for curves, why horizontal tangents "
        "can deceive us, and how engineering systems achieve peak efficiency through extremum principles."
    )

    # -------------------------------------------------------------
    # SLIDE 2: Lecture Roadmap
    # -------------------------------------------------------------
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_background(s2)
    add_header(s2, "Lecture Trajectory: From Kinetic Intuition to Optimization")
    
    modules = [
        ("01", "Visual Motion & Critical Intuition", "Moving tangent vectors, slope zero conditions, and singularities (corners/cusps).", CYAN),
        ("02", "First Derivative Test & Sign Charts", "Factorization morphing, interval sign sampling, and direction transitions.", AMBER),
        ("03", "Second Derivative & Concavity Bending", "Differential curvature f''(x), concavity bowls, and inflection terraces.", CORAL),
        ("04", "Closed-Interval Engineering Optimization", "Extreme Value Theorem, candidate matrix, and Maximum Power Transfer.", GREEN),
    ]
    for i, (num, title, desc, accent) in enumerate(modules):
        col_left = Inches(0.8 + i * 2.98)
        c = add_card(s2, col_left, Inches(1.7), Inches(2.8), Inches(4.8), border_color=accent)
        tb = s2.shapes.add_textbox(col_left + Inches(0.2), Inches(1.9), Inches(2.4), Inches(4.4))
        tf = tb.text_frame
        tf.word_wrap = True
        
        p = tf.paragraphs[0]
        p.text = num
        p.font.size = Pt(28)
        p.font.bold = True
        p.font.color.rgb = accent
        
        p2 = tf.add_paragraph()
        p2.text = title
        p2.font.size = Pt(16)
        p2.font.bold = True
        p2.font.color.rgb = TEXT_WHITE
        p2.space_before = Pt(10)
        
        p3 = tf.add_paragraph()
        p3.text = desc
        p3.font.size = Pt(12)
        p3.font.color.rgb = TEXT_MUTED
        p3.space_before = Pt(12)

    # -------------------------------------------------------------
    # Helper to add a Video + Notes Slide
    # -------------------------------------------------------------
    def add_video_slide(prs, title, video_path, frame_path, subtitle, prompt_text, notes):
        s = prs.slides.add_slide(blank_layout)
        set_slide_background(s)
        add_header(s, title)
        
        # Video on Left
        vid_left = Inches(0.8)
        vid_top = Inches(1.5)
        vid_w = Inches(7.8)
        vid_h = Inches(4.387)
        # Borderless seamless video embedding
        try:
            s.shapes.add_movie(video_path, vid_left, vid_top, vid_w, vid_h, poster_frame_image=frame_path, mime_type='video/mp4')
        except Exception:
            # Fallback to poster frame
            s.shapes.add_picture(frame_path, vid_left, vid_top, vid_w, vid_h)
            
        # Side Teaching Guidance Card
        side_card = add_card(s, Inches(8.9), Inches(1.5), Inches(3.633), Inches(5.4), border_color=CARD_BORDER)
        tb_side = s.shapes.add_textbox(Inches(9.1), Inches(1.7), Inches(3.233), Inches(5.0))
        tf_side = tb_side.text_frame
        tf_side.word_wrap = True
        
        p = tf_side.paragraphs[0]
        p.text = "KEY TEACHING OBJECTIVE"
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = AMBER
        
        p2 = tf_side.add_paragraph()
        p2.text = subtitle
        p2.font.size = Pt(14)
        p2.font.bold = True
        p2.font.color.rgb = TEXT_WHITE
        p2.space_before = Pt(8)
        
        p3 = tf_side.add_paragraph()
        p3.text = "LECTURE PROMPT & PAUSE CUE"
        p3.font.size = Pt(11)
        p3.font.bold = True
        p3.font.color.rgb = CYAN
        p3.space_before = Pt(16)
        
        p4 = tf_side.add_paragraph()
        p4.text = prompt_text
        p4.font.size = Pt(12)
        p4.font.color.rgb = TEXT_MUTED
        p4.space_before = Pt(8)

        # Bottom play hint
        p5 = tf_side.add_paragraph()
        p5.text = "[Tap video to play animation on iPad]"
        p5.font.size = Pt(10)
        p5.font.color.rgb = TEXT_MUTED
        p5.space_before = Pt(24)

        s.notes_slide.notes_text_frame.text = notes
        return s

    # Helper to add an Apple Pencil Annotation Slide
    def add_annotation_slide(prs, title, frame_path, exercise_title, instructions, pencil_prompts, notes):
        s = prs.slides.add_slide(blank_layout)
        set_slide_background(s)
        add_header(s, title, category="LIVE ANNOTATION WORKSPACE // APPLE PENCIL INTERACTION")
        
        # Left side: Reference visual frame
        f_left = Inches(0.8)
        f_top = Inches(1.5)
        f_w = Inches(6.0)
        f_h = Inches(3.375)
        add_card(s, f_left - Inches(0.05), f_top - Inches(0.05), f_w + Inches(0.1), f_h + Inches(0.1), border_color=AMBER)
        s.shapes.add_picture(frame_path, f_left, f_top, f_w, f_h)
        
        # Under image: key formula/summary card
        bot_card = add_card(s, Inches(0.8), Inches(5.1), Inches(6.0), Inches(1.8), border_color=CARD_BORDER)
        tb_bot = s.shapes.add_textbox(Inches(1.0), Inches(5.2), Inches(5.6), Inches(1.6))
        tf_bot = tb_bot.text_frame
        tf_bot.word_wrap = True
        p = tf_bot.paragraphs[0]
        p.text = "ANALYTIC FORMULATION & CHECKLIST"
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = CYAN
        for inst in instructions:
            pi = tf_bot.add_paragraph()
            pi.text = "• " + inst
            pi.font.size = Pt(11)
            pi.font.color.rgb = TEXT_WHITE
            pi.space_before = Pt(4)

        # Right side: Full Live Apple Pencil Derivation Canvas Box
        c_right = add_card(s, Inches(7.1), Inches(1.5), Inches(5.433), Inches(5.4), border_color=CYAN, bg_color=RGBColor(15, 23, 42))
        tb_c = s.shapes.add_textbox(Inches(7.3), Inches(1.7), Inches(5.033), Inches(5.0))
        tf_c = tb_c.text_frame
        tf_c.word_wrap = True
        
        p = tf_c.paragraphs[0]
        p.text = "APPLE PENCIL SCRATCHPAD: " + exercise_title.upper()
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = CYAN
        
        p2 = tf_c.add_paragraph()
        p2.text = "Live Student Derivation Prompts:"
        p2.font.size = Pt(13)
        p2.font.bold = True
        p2.font.color.rgb = TEXT_WHITE
        p2.space_before = Pt(8)
        
        for prompt in pencil_prompts:
            pp = tf_c.add_paragraph()
            pp.text = "✍️ " + prompt
            pp.font.size = Pt(12)
            pp.font.color.rgb = TEXT_MUTED
            pp.space_before = Pt(12)

        s.notes_slide.notes_text_frame.text = notes
        return s

    # -------------------------------------------------------------
    # SLIDE 3: Scene 01 Video - Hook Hill
    # -------------------------------------------------------------
    add_video_slide(
        prs,
        title="Terrain Exploration: The Geometry of Peaks & Valleys",
        video_path="media/videos/clips/Scene01_HookHill.mp4",
        frame_path="media/frames/Scene01_HookHill_frame.png",
        subtitle="Identifying Extrema along an Elevation Profile",
        prompt_text="Ask the lecture hall: 'As our exploration probe traverses this mountain range, what exact instantaneous property characterizes the true summits and lowest valleys?'",
        notes="Play the animation. Note how the probe ascends and descends. Highlight that slope is positive on ascent, zero at crests, negative on descent."
    )

    # -------------------------------------------------------------
    # SLIDE 4: Scene 01 Annotation - Slope Intuition
    # -------------------------------------------------------------
    add_annotation_slide(
        prs,
        title="Live Annotation: Direction of Motion & Tangent Equilibrium",
        frame_path="media/frames/Scene01_HookHill_frame.png",
        exercise_title="Terrain Tangent Incline",
        instructions=[
            "Increasing interval: Rate of climb f'(x) > 0",
            "Peak crest: Instantaneous horizontal leveling f'(x) = 0",
            "Decreasing interval: Rate of descent f'(x) < 0",
            "Valley floor: Leveling out before re-ascent f'(x) = 0"
        ],
        pencil_prompts=[
            "Draw tangent lines with Apple Pencil at x = -2.5, x = -1.2, x = 0, and x = 1.8.",
            "Write the algebraic inequality for slope: m > 0 vs. m = 0 vs. m < 0.",
            "Circle the global highest point vs local sub-crest."
        ],
        notes="Engage students by sketching tangent arrows live. Emphasize that zero slope is the boundary marker between climbing and falling."
    )

    # -------------------------------------------------------------
    # SLIDE 5: Scene 02 Video - Local vs Absolute
    # -------------------------------------------------------------
    add_video_slide(
        prs,
        title="Topological Definitions: Local vs. Absolute Extrema",
        video_path="media/videos/clips/Scene02_LocalVsAbsolute.mp4",
        frame_path="media/frames/Scene02_LocalVsAbsolute_frame.png",
        subtitle="Open Neighborhoods vs. Entire Domain Supremum",
        prompt_text="Key Conceptual Question: 'Can a local maximum have a lower numerical value than a local minimum in the same function?'",
        notes="Play clip. Clarify that 'Local' requires an open ball (c-delta, c+delta), whereas 'Absolute' compares against all x in domain D."
    )

    # -------------------------------------------------------------
    # SLIDE 6: Scene 02 Annotation - Boundary Extrema
    # -------------------------------------------------------------
    add_annotation_slide(
        prs,
        title="Live Annotation: The Neighborhood Test & Boundary Caps",
        frame_path="media/frames/Scene02_LocalVsAbsolute_frame.png",
        exercise_title="Neighborhood Verification",
        instructions=[
            "Local Max: f(c) >= f(x) for all x in (c - delta, c + delta)",
            "Boundary points on [a, b] cannot contain two-sided open intervals!",
            "Therefore: Boundary endpoints CANNOT be Local Extrema (by standard definition).",
            "Endpoints CAN and frequently DO serve as Absolute Extrema!"
        ],
        pencil_prompts=[
            "Draw an open interval (c - δ, c + δ) around the local peak.",
            "Show why the endpoint x = b cannot fit a two-sided ball.",
            "Annotate why the right boundary is the Global Maximum."
        ],
        notes="This distinction prevents severe exam errors. Reinforce that local extrema are interior phenomena."
    )

    # -------------------------------------------------------------
    # SLIDE 7: MASTER SEQUENCE (THE FULL CONTINUOUS 3BLUE1BROWN MOVIE)
    # -------------------------------------------------------------
    add_video_slide(
        prs,
        title="🌟 Unified Master Sequence: The Cubic Manifold",
        video_path="media/videos/clips/SignatureSequenceMaster.mp4",
        frame_path="media/frames/SignatureSequenceMaster_frame.png",
        subtitle="Continuous 3Blue1Brown Kinematic Derivation of f(x) = x³ - 3x",
        prompt_text="Watch the complete sequence flow: curve creation, dynamic rotating slope tangent, equation morphing 3x² - 3 -> 3(x-1)(x+1) = 0, and concavity verification.",
        notes="Play the continuous master animation. Tap video to pause and discuss any intermediate step with Apple Pencil."
    )

    # -------------------------------------------------------------
    # SLIDE 8: Signature Scene 1 Video - The Cubic Curve
    # -------------------------------------------------------------
    add_video_slide(
        prs,
        title="Signature Function: f(x) = x³ - 3x Trajectory",
        video_path="media/videos/clips/SignatureScene1_TheFunction.mp4",
        frame_path="media/frames/SignatureScene1_TheFunction_frame.png",
        subtitle="Tracking the Coordinate State of an Odd Cubic Curve",
        prompt_text="Observe the symmetry: f(-x) = -f(x). What does odd symmetry tell us about the relationship between maxima and minima?",
        notes="Introduce f(x) = x^3 - 3x as the primary worked model. Point travels from x = -2.2 to x = 2.2, traversing a crest and a trough."
    )

    # -------------------------------------------------------------
    # SLIDE 8: Signature Scene 2 Video - The Dynamic Tangent
    # -------------------------------------------------------------
    add_video_slide(
        prs,
        title="Kinetic Tangent: Dynamic Slope Telemetry",
        video_path="media/videos/clips/SignatureScene2_TheTangent.mp4",
        frame_path="media/frames/SignatureScene2_TheTangent_frame.png",
        subtitle="Visualizing the Derivative as an Instantaneous Vector",
        prompt_text="Notice the real-time slope readout: as the point passes x = -1, the slope m collapses precisely from positive to zero to negative.",
        notes="Play the clip. Point out the color change of the tangent line: Cyan (positive slope) to Amber (zero slope) to Coral (negative slope)."
    )

    # -------------------------------------------------------------
    # SLIDE 9: Signature Scene 2 Annotation - Tangent Slope Derivation
    # -------------------------------------------------------------
    add_annotation_slide(
        prs,
        title="Live Annotation: Instantaneous Slope Derivation",
        frame_path="media/frames/SignatureScene2_TheTangent_frame.png",
        exercise_title="Differentiation from First Principles",
        instructions=[
            "Given: f(x) = x³ - 3x",
            "Derivative: f'(x) = d/dx [x³ - 3x] = 3x² - 3",
            "At x = -1: f'(-1) = 3(-1)² - 3 = 0  (Horizontal)",
            "At x = 0:  f'(0)  = 3(0)² - 3 = -3  (Steepest descent)"
        ],
        pencil_prompts=[
            "Derive f'(x) step-by-step using the Power Rule.",
            "Calculate f'(0) live and write why this represents maximum descent rate.",
            "Calculate f'(1) and verify the second horizontal tangent."
        ],
        notes="Guide the students through applying the power rule live. Write down the derivative in the scratchpad."
    )

    # -------------------------------------------------------------
    # SLIDE 10: Scene 03 Video - Singularities DNE
    # -------------------------------------------------------------
    add_video_slide(
        prs,
        title="Singularities: When Derivatives Fail to Exist",
        video_path="media/videos/clips/Scene03_SingularitiesDNE.mp4",
        frame_path="media/frames/Scene03_SingularitiesDNE_frame.png",
        subtitle="Critical Points Beyond Smooth Tangents: Corners & Cusps",
        prompt_text="Critical Challenge: 'Does a curve need a smooth horizontal tangent to have an absolute minimum? Look at |x| and x^(2/3).'",
        notes="Play clip. Critical numbers occur where f'(c) = 0 OR where f'(c) does not exist (DNE), provided c is in the domain!"
    )

    # -------------------------------------------------------------
    # SLIDE 11: Scene 03 Annotation - Non-Differentiable Extrema
    # -------------------------------------------------------------
    add_annotation_slide(
        prs,
        title="Live Annotation: Left vs. Right Difference Quotients",
        frame_path="media/frames/Scene03_SingularitiesDNE_frame.png",
        exercise_title="Singularity Limit Analysis",
        instructions=[
            "Absolute Value f(x) = |x| at x = 0: lim(x->0-) = -1 != lim(x->0+) = +1",
            "Power Function f(x) = x^(2/3): f'(x) = (2/3)x^(-1/3) = 2/(3 * x^(1/3))",
            "As x -> 0, f'(x) -> ±∞ (Vertical Tangent / Cusp)",
            "Both functions reach a valid, indisputable Global Minimum at (0, 0)!"
        ],
        pencil_prompts=[
            "Compute lim_{h->0-} and lim_{h->0+} for |h|/h live.",
            "Write the formal two-part definition of Critical Number c: (1) f'(c)=0 OR (2) f'(c) DNE, with c in Domain.",
            "Highlight common student trap: 'Assuming critical points only come from setting derivative equal to 0'."
        ],
        notes="Crucial misconception buster: many students forget to test points where denominator of f'(x) is zero."
    )

    # -------------------------------------------------------------
    # SLIDE 12: Signature Scene 7 Video - Counterexample g(x)=x^3
    # -------------------------------------------------------------
    add_video_slide(
        prs,
        title="The Critical Trap: When f'(c) = 0 Yields NO Extremum",
        video_path="media/videos/clips/SignatureScene7_Counterexample.mp4",
        frame_path="media/frames/SignatureScene7_Counterexample_frame.png",
        subtitle="Stationary Inflection Point on g(x) = x³",
        prompt_text="Examine g(x) = x³: g'(0) = 0. The tangent is perfectly horizontal. Is (0, 0) a maximum or a minimum?",
        notes="Play clip. Tangent line goes horizontal at x=0, but the curve continues climbing. Zero derivative is NECESSARY, not SUFFICIENT."
    )

    # -------------------------------------------------------------
    # SLIDE 13: Signature Scene 7 Annotation - Terrace Logic
    # -------------------------------------------------------------
    add_annotation_slide(
        prs,
        title="Live Annotation: Inflection Terraces & Necessary vs. Sufficient",
        frame_path="media/frames/SignatureScene7_Counterexample_frame.png",
        exercise_title="Logical Counterexample Proof",
        instructions=[
            "Theorem (Fermat's): If f has a local extremum at c and f'(c) exists, then f'(c) = 0.",
            "Converse: 'If f'(c) = 0, then f has an extremum at c' is FALSE!",
            "For g(x) = x³: g'(x) = 3x² >= 0 for all x.",
            "Sign test: (+) before 0, and (+) after 0. No sign reversal!"
        ],
        pencil_prompts=[
            "Write the logic implication: Extremum => f'(c)=0 (True), f'(c)=0 => Extremum (False).",
            "Sketch the sign line for 3x² showing (+) -> (0) -> (+).",
            "Define 'Stationary Inflection Point' (Horizontal inflection point)."
        ],
        notes="Draw attention to logic arrows: P => Q does not mean Q => P. This is tested on every university exam."
    )

    # -------------------------------------------------------------
    # SLIDE 14: Signature Scene 3 Video - Equation Morphing
    # -------------------------------------------------------------
    add_video_slide(
        prs,
        title="Algebraic Morphing: Factoring the Derivative",
        video_path="media/videos/clips/SignatureScene3_EquationMorph.mp4",
        frame_path="media/frames/SignatureScene3_EquationMorph_frame.png",
        subtitle="3x² - 3  ==>  3(x² - 1)  ==>  3(x - 1)(x + 1) = 0",
        prompt_text="Notice how the algebraic zeros x = -1 and x = +1 project vertically into physical coordinates on the function curve.",
        notes="Play clip. Point out how factoring reveals the exact roots where the velocity of the curve momentarily freezes."
    )

    # -------------------------------------------------------------
    # SLIDE 15: Signature Scene 4 Video - First Derivative Test
    # -------------------------------------------------------------
    add_video_slide(
        prs,
        title="First Derivative Test: Dynamic Sign Partitioning",
        video_path="media/videos/clips/SignatureScene4_DerivativeTest.mp4",
        frame_path="media/frames/SignatureScene4_DerivativeTest_frame.png",
        subtitle="Number Line Sampling & Directional Transitions",
        prompt_text="Watch the sign chart reveal: positive slopes push the curve up, zero halts it, negative slopes pull it down.",
        notes="Play clip. The number line is partitioned by critical numbers into (-inf, -1), (-1, 1), and (1, inf)."
    )

    # -------------------------------------------------------------
    # SLIDE 16: Signature Scene 4 Annotation - Sign Chart Construction
    # -------------------------------------------------------------
    add_annotation_slide(
        prs,
        title="Live Annotation: First Derivative Sign Chart Matrix",
        frame_path="media/frames/SignatureScene4_DerivativeTest_frame.png",
        exercise_title="Interval Test Table",
        instructions=[
            "Interval 1: (-inf, -1) -> Test x = -2: f'(-2) = 3(-2)² - 3 = +9 > 0 (INC)",
            "Interval 2: (-1, 1)    -> Test x = 0:  f'(0) = 3(0)² - 3 = -3 < 0   (DEC)",
            "Interval 3: (1, inf)   -> Test x = +2: f'(+2) = 3(2)² - 3 = +9 > 0  (INC)",
            "Conclusion: (+ to -) traps a LOCAL MAX; (- to +) holds a LOCAL MIN."
        ],
        pencil_prompts=[
            "Draw the 3-row sign chart table with Apple Pencil.",
            "Fill in test values and show factor signs: (x-1) and (x+1).",
            "Draw the physical climbing/falling arrows: ↗ ↘ ↗."
        ],
        notes="Show students the factored testing method: instead of computing 3x^2-3, check signs of 3*(x-1)*(x+1) directly."
    )

    # -------------------------------------------------------------
    # SLIDE 17: Signature Scene 5 Video & Slide - Exact Extrema
    # -------------------------------------------------------------
    add_video_slide(
        prs,
        title="Coordinate Verification: Locating Exact Extrema",
        video_path="media/videos/clips/SignatureScene5_ExtremaReveal.mp4",
        frame_path="media/frames/SignatureScene5_ExtremaReveal_frame.png",
        subtitle="Evaluating Critical Numbers in the ORIGINAL Function f(x)",
        prompt_text="Common blunder alert: Students plug x = -1 into f'(x) and get 0! Where must we substitute to find the height of the curve?",
        notes="Play clip. Emphasize: f(-1) = (-1)^3 - 3(-1) = -1 + 3 = +2 -> Local Max (-1, 2). f(1) = (1)^3 - 3(1) = -2 -> Local Min (1, -2)."
    )

    # -------------------------------------------------------------
    # SLIDE 18: Signature Scene 6 Video - Second Derivative & Concavity
    # -------------------------------------------------------------
    add_video_slide(
        prs,
        title="Second Derivative Test: Curvature & Concavity Bending",
        video_path="media/videos/clips/SignatureScene6_SecondDerivative.mp4",
        frame_path="media/frames/SignatureScene6_SecondDerivative_frame.png",
        subtitle="f''(x) = 6x Measures the Rate of Change of Slope",
        prompt_text="Physical Intuition: If f'(x) = 0 and f''(x) < 0, slopes are decreasing (positive -> 0 -> negative). The curve MUST be concave down (trapping a peak).",
        notes="Play clip. Note the two visual bowls: Concave Down (cap) with negative second derivative, Concave Up (cup) with positive second derivative."
    )

    # -------------------------------------------------------------
    # SLIDE 19: Test Comparison & Decision Matrix
    # -------------------------------------------------------------
    s19 = prs.slides.add_slide(blank_layout)
    set_slide_background(s19)
    add_header(s19, "Extrema Decision Matrix: 1st vs. 2nd Derivative Test", category="THEORETICAL COMPARISON // EXAM STRATEGY")
    
    # Left Card: 1st Derivative Test
    c_left = add_card(s19, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.4), border_color=CYAN)
    tb_l = s19.shapes.add_textbox(Inches(1.0), Inches(1.7), Inches(5.2), Inches(5.0))
    tf_l = tb_l.text_frame
    tf_l.word_wrap = True
    p = tf_l.paragraphs[0]
    p.text = "FIRST DERIVATIVE TEST"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = CYAN
    
    items_l = [
        ("Applicability", "Universal. Works for smooth points AND singularities (corners/cusps)."),
        ("Mechanism", "Checks sign change of f'(x) across x = c."),
        ("Outcomes", "(+ to -) => Local Max\n(- to +) => Local Min\n(No change) => Neither"),
        ("Limitation", "Requires picking test points in every interval."),
        ("Verdict", "Always reliable. Fallback when 2nd test fails.")
    ]
    for k, v in items_l:
        p1 = tf_l.add_paragraph()
        p1.text = k.upper()
        p1.font.size = Pt(11)
        p1.font.bold = True
        p1.font.color.rgb = AMBER
        p1.space_before = Pt(8)
        p2 = tf_l.add_paragraph()
        p2.text = v
        p2.font.size = Pt(11)
        p2.font.color.rgb = TEXT_WHITE

    # Right Card: 2nd Derivative Test
    c_right = add_card(s19, Inches(6.9), Inches(1.5), Inches(5.6), Inches(5.4), border_color=AMBER)
    tb_r = s19.shapes.add_textbox(Inches(7.1), Inches(1.7), Inches(5.2), Inches(5.0))
    tf_r = tb_r.text_frame
    tf_r.word_wrap = True
    p = tf_r.paragraphs[0]
    p.text = "SECOND DERIVATIVE TEST"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = AMBER
    
    items_r = [
        ("Applicability", "Restricted. Requires f'(c) = 0 and f''(c) to exist."),
        ("Mechanism", "Evaluates single point concavity f''(c) directly."),
        ("Outcomes", "f''(c) < 0 => Concave Down => Local Max\nf''(c) > 0 => Concave Up => Local Min\nf''(c) = 0 => INCONCLUSIVE (Must use 1st test!)"),
        ("Limitation", "Fails on cusps, corners, and flat inflection points."),
        ("Verdict", "Faster when differentiation is easy, but fragile.")
    ]
    for k, v in items_r:
        p1 = tf_r.add_paragraph()
        p1.text = k.upper()
        p1.font.size = Pt(11)
        p1.font.bold = True
        p1.font.color.rgb = CYAN
        p1.space_before = Pt(8)
        p2 = tf_r.add_paragraph()
        p2.text = v
        p2.font.size = Pt(11)
        p2.font.color.rgb = TEXT_WHITE

    s19.notes_slide.notes_text_frame.text = (
        "LECTURE EMPHASIS:\n"
        "Stress the 'Inconclusive' case: for f(x)=x^4, f''(0)=0 and it has a min.\n"
        "For f(x)=-x^4, f''(0)=0 and it has a max. For f(x)=x^3, f''(0)=0 and it has neither!\n"
        "If f''(c)=0, never guess. Revert immediately to the First Derivative Test."
    )

    # -------------------------------------------------------------
    # SLIDE 20: Scene 04 Video - Closed Interval Method
    # -------------------------------------------------------------
    add_video_slide(
        prs,
        title="Closed Interval Method: The Extreme Value Theorem",
        video_path="media/videos/clips/Scene04_ClosedIntervalMethod.mp4",
        frame_path="media/frames/Scene04_ClosedIntervalMethod_frame.png",
        subtitle="f(x) = x³ - 3x Restricted to the Closed Interval [-0.5, 2.5]",
        prompt_text="Notice how the local maximum at x = -1 is EXCLUDED because it lies outside [-0.5, 2.5]! Where does the absolute maximum occur?",
        notes="Play clip. Candidate evaluation: interior critical point x=1 -> f(1)=-2. Endpoints: x=-0.5 -> f(-0.5)=1.375; x=2.5 -> f(2.5)=8.125 (Winner!)."
    )

    # -------------------------------------------------------------
    # SLIDE 21: Scene 05 Video - Engineering Optimization
    # -------------------------------------------------------------
    add_video_slide(
        prs,
        title="Engineering Optimization: Maximum Power Transfer Theorem",
        video_path="media/videos/clips/Scene05_MaxPowerTransfer.mp4",
        frame_path="media/frames/Scene05_MaxPowerTransfer_frame.png",
        subtitle="Maximizing Load Power P(R_L) = V_th² * R_L / (R_th + R_L)²",
        prompt_text="Differentiating with the Quotient Rule reveals: dP/dR_L = 0 occurs precisely when R_load = R_thevenin! Impedance matching in RF and audio circuits.",
        notes="Play clip. Highlight the engineering trade-off: at R_L = 0, current is maximum but voltage is 0 (P=0). At R_L = inf, voltage is maximum but current is 0 (P=0)."
    )

    # -------------------------------------------------------------
    # SLIDE 22: Practice Problem & Exit Ticket
    # -------------------------------------------------------------
    s22 = prs.slides.add_slide(blank_layout)
    set_slide_background(s22)
    add_header(s22, "Engineering Practice Challenge & Exit Ticket", category="STUDENT ACTIVE LEARNING // LIVE DERIVATION")
    
    # Left Card: Problem Statement
    c_prob = add_card(s22, Inches(0.8), Inches(1.5), Inches(5.8), Inches(5.4), border_color=AMBER)
    tb_pr = s22.shapes.add_textbox(Inches(1.0), Inches(1.7), Inches(5.4), Inches(5.0))
    tf_pr = tb_pr.text_frame
    tf_pr.word_wrap = True
    p = tf_pr.paragraphs[0]
    p.text = "ACTIVE LEARNING CHALLENGE"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = AMBER
    
    p2 = tf_pr.add_paragraph()
    p2.text = "Analyze the structural response function:"
    p2.font.size = Pt(12)
    p2.font.color.rgb = TEXT_WHITE
    p2.space_before = Pt(6)
    
    p3 = tf_pr.add_paragraph()
    p3.text = "f(x) = 2x³ - 3x² - 12x + 5   on   [-2, 4]"
    p3.font.size = Pt(16)
    p3.font.bold = True
    p3.font.color.rgb = CYAN
    p3.space_before = Pt(8)

    steps = [
        "1. Compute f'(x) and factor completely.",
        "2. Identify all critical numbers inside [-2, 4].",
        "3. Apply Second Derivative Test to classify local extrema.",
        "4. Construct the EVT candidate table (criticals + endpoints).",
        "5. Identify Global Maximum and Global Minimum coordinates."
    ]
    for step in steps:
        ps = tf_pr.add_paragraph()
        ps.text = step
        ps.font.size = Pt(11)
        ps.font.color.rgb = TEXT_MUTED
        ps.space_before = Pt(6)

    # Right Card: Progressive Solution Key (for Instructor or Reveal)
    c_sol = add_card(s22, Inches(6.9), Inches(1.5), Inches(5.633), Inches(5.4), border_color=CYAN)
    tb_s = s22.shapes.add_textbox(Inches(7.1), Inches(1.7), Inches(5.233), Inches(5.0))
    tf_s = tb_s.text_frame
    tf_s.word_wrap = True
    p = tf_s.paragraphs[0]
    p.text = "SOLUTION CHECKLIST & ANSWER KEY"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = CYAN
    
    sol_lines = [
        ("Derivative:", "f'(x) = 6x² - 6x - 12 = 6(x - 2)(x + 1)"),
        ("Critical Numbers:", "x = -1   and   x = 2   (both inside [-2, 4])"),
        ("Second Derivative:", "f''(x) = 12x - 6"),
        ("At x = -1:", "f''(-1) = -18 < 0  =>  Local Max at (-1, 12)"),
        ("At x = 2:", "f''(2) = +18 > 0   =>  Local Min at (2, -15)"),
        ("Candidate Table:", "f(-2) = 1\nf(-1) = 12\nf(2)  = -15\nf(4)  = 37"),
        ("Global Extrema:", "Global Max: (4, 37)  [Endpoint!]\nGlobal Min: (2, -15) [Interior Critical!]")
    ]
    for lbl, val in sol_lines:
        pl = tf_s.add_paragraph()
        pl.text = lbl.upper()
        pl.font.size = Pt(10)
        pl.font.bold = True
        pl.font.color.rgb = AMBER
        pl.space_before = Pt(6)
        pv = tf_s.add_paragraph()
        pv.text = val
        pv.font.size = Pt(11)
        pv.font.color.rgb = TEXT_WHITE

    s22.notes_slide.notes_text_frame.text = (
        "INSTRUCTOR WRAP-UP & EXIT TICKET:\n"
        "Give students 4 minutes to work. Walk the room or display Apple Pencil annotations.\n"
        "Reveal the key insight: The local max (-1, 12) is soundly beaten by the endpoint (4, 37)!\n"
        "Remind students: Never neglect endpoints in engineering optimization."
    )

    # -------------------------------------------------------------
    # SLIDE 23: Mathalino Problem 1 - Number Optimization Video
    # -------------------------------------------------------------
    add_video_slide(
        prs,
        title="Mathalino Prob 1: Number Exceeding its Square",
        video_path="media/videos/clips/MathalinoProblem1_NumberOptimization.mp4",
        frame_path="media/frames/MathalinoProblem1_NumberOptimization_frame.png",
        subtitle="What number exceeds its square by the maximum amount? (Source: mathalino.com)",
        prompt_text="Objective f(x) = x - x². Differentiating f'(x) = 1 - 2x = 0 yields critical number x = 1/2. Concavity f''(x) = -2 < 0 proves strict global maximum of 1/4.",
        notes="Mathalino Prob 1. Source: mathalino.com/reviewer/differential-calculus/01-04-number-problems-in-maxima-and-minima. Emphasize model definition, derivative test, and concavity."
    )

    # SLIDE 24: Mathalino Problem 1 - Annotation Workspace
    add_annotation_slide(
        prs,
        title="Mathalino Prob 1: Modeling & Solution Workspace",
        frame_path="media/frames/MathalinoProblem1_NumberOptimization_frame.png",
        exercise_title="Number Optimization (Mathalino 01)",
        instructions=[
            "Define variable x as the unknown number.",
            "Formulate objective function: f(x) = x - x².",
            "Differentiate and find critical number: f'(x) = 1 - 2x = 0 => x = 1/2.",
            "Verify with 2nd derivative: f''(1/2) = -2 < 0 (Maximum).",
            "Calculate maximum excess value: f(1/2) = 1/4."
        ],
        pencil_prompts=[
            "✍️ Write out the objective function f(x) and its derivative f'(x).",
            "✍️ Solve for critical number and compute second derivative f''(x).",
            "✍️ State final conclusion: number is 1/2, maximum excess is 1/4."
        ],
        notes="Instructor Guidance: Walk students through translating English problem statement into calculus objective function."
    )

    # -------------------------------------------------------------
    # SLIDE 25: Mathalino Problem 10 - Riverbank Fencing Video
    # -------------------------------------------------------------
    add_video_slide(
        prs,
        title="Mathalino Prob 10: Riverbank Fencing Optimization",
        video_path="media/videos/clips/MathalinoProblem2_RiverbankLot.mp4",
        frame_path="media/frames/MathalinoProblem2_RiverbankLot_frame.png",
        subtitle="Least fencing perimeter for fixed area A along a riverbank (Source: mathalino.com)",
        prompt_text="Area A = xy reduces perimeter P = x + 2y to single variable P(y) = A/y + 2y. Differentiating: dP/dy = -A/y² + 2 = 0 => 2y² = A = xy => Width y = x/2.",
        notes="Mathalino Prob 10. Source: mathalino.com/reviewer/differential-calculus/09-11-rectangular-lot-problems-in-maxima-and-minima. Geometric constraint reduces multivariable to single variable. Optimal shape: width is half length."
    )

    # SLIDE 26: Mathalino Problem 10 - Annotation Workspace
    add_annotation_slide(
        prs,
        title="Mathalino Prob 10: Fencing Constraint Workspace",
        frame_path="media/frames/MathalinoProblem2_RiverbankLot_frame.png",
        exercise_title="Riverbank Fencing (Mathalino 10)",
        instructions=[
            "Identify given constraint: Constant Area A = xy.",
            "Express objective fence length: P = x + 2y (no fence along river).",
            "Substitute x = A/y to obtain single-variable function P(y).",
            "Differentiate dP/dy = -A/y² + 2 = 0 => 2y² = A.",
            "Substitute A = xy: 2y² = xy => y = (1/2)x (width is half length)."
        ],
        pencil_prompts=[
            "✍️ Sketch the riverbank and the 3-sided fence.",
            "✍️ Substitute constraint x = A/y into P = x + 2y.",
            "✍️ Differentiate and prove that optimal width y = (1/2)x."
        ],
        notes="Instructor Guidance: Contrast 3-sided fence (y = x/2) with traditional 4-sided enclosure (square x = y)."
    )

    # -------------------------------------------------------------
    # SLIDE 27: Mathalino Problem 16 - Open-Top Box Video
    # -------------------------------------------------------------
    add_video_slide(
        prs,
        title="Mathalino Prob 16: Open-Top Box Optimization",
        video_path="media/videos/clips/MathalinoProblem3_OpenTopBox.mp4",
        frame_path="media/frames/MathalinoProblem3_OpenTopBox_frame.png",
        subtitle="15\" × 24\" Cardboard Sheet: Cut squares x to maximize Volume (Source: mathalino.com)",
        prompt_text="V(x) = (24-2x)(15-2x)x = 4x³ - 78x² + 360x. Setting V'(x) = 0 yields x = 3 or x = 10. Feasible physical domain (0, 7.5) eliminates x = 10! V_max = 486 in³.",
        notes="Mathalino Prob 16. Source: mathalino.com/reviewer/differential-calculus/15-17-box-open-at-the-top. Critical points must be tested against physical boundaries. x=10 is extraneous because 15-2(10) < 0."
    )

    # SLIDE 28: Mathalino Problem 16 - Annotation Workspace
    add_annotation_slide(
        prs,
        title="Mathalino Prob 16: Domain Feasibility & Volume Workspace",
        frame_path="media/frames/MathalinoProblem3_OpenTopBox_frame.png",
        exercise_title="Open-Top Box Optimization (Mathalino 16)",
        instructions=[
            "Cardboard dimensions: 24'' by 15''. Corner cutout: x by x.",
            "Folded dimensions: Length = 24 - 2x, Width = 15 - 2x, Height = x.",
            "Objective: V(x) = 4x³ - 78x² + 360x.",
            "Differentiate: V'(x) = 12(x² - 13x + 30) = 12(x - 3)(x - 10) = 0.",
            "Physical domain check: 0 < x < 7.5''. Reject x = 10''.",
            "Optimal cut x = 3''. V_max = (18)(9)(3) = 486 in³."
        ],
        pencil_prompts=[
            "✍️ Write dimensions of folded box in terms of x.",
            "✍️ Factor V'(x) = 0 and solve for critical numbers x = 3, 10.",
            "✍️ Disqualify x = 10 using width constraint 15 - 2x > 0.",
            "✍️ Compute maximum volume V(3) = 486 in³."
        ],
        notes="Instructor Guidance: Emphasize why domain inspection is mandatory in engineering optimization."
    )

    # -------------------------------------------------------------
    # SLIDE 29: Mathalino Problem 03 - Tour Bus Revenue Video
    # -------------------------------------------------------------
    add_video_slide(
        prs,
        title="Mathalino Prob 03: Tour Bus Maximum Revenue",
        video_path="media/videos/clips/MathalinoProblem4_TourBusRevenue.mp4",
        frame_path="media/frames/MathalinoProblem4_TourBusRevenue_frame.png",
        subtitle="80-Seat Tour Bus: Balancing ticket price vs. demand drop (Source: mathalino.com)",
        prompt_text="Base fare: P350/seat. Increments: P12.50/seat with -2 passengers. R(x) = (350 + 12.5x)(80 - 2x) = 28,000 + 300x - 25x². dR/dx = 0 => x = 6. Fare = P425, Revenue = P28,900 [Option C].",
        notes="Mathalino Prob 03. Source: mathalino.com/reviewer/differential-calculus/03-maximum-revenue-tour-bus-80-seats. Real-world business revenue optimization. Matches Option C on Mathalino reviewer."
    )

    # SLIDE 30: Mathalino Problem 03 - Annotation Workspace
    add_annotation_slide(
        prs,
        title="Mathalino Prob 03: Revenue Model Workspace",
        frame_path="media/frames/MathalinoProblem4_TourBusRevenue_frame.png",
        exercise_title="Tour Bus Revenue (Mathalino 03)",
        instructions=[
            "Base fare: P28,000 / 80 seats = P350 per passenger.",
            "Increment per seat: P1,000 / 80 = P12.50 per passenger.",
            "Let x = number of P1,000 package increments.",
            "Price p(x) = 350 + 12.5x; Demand q(x) = 80 - 2x.",
            "R(x) = 28,000 + 300x - 25x² => dR/dx = 300 - 50x = 0 => x = 6.",
            "Optimal Fare: P425/seat; Passengers: 68; Max Revenue: P28,900."
        ],
        pencil_prompts=[
            "✍️ Formulate price p(x) and quantity q(x) expressions.",
            "✍️ Multiply to construct R(x) and differentiate dR/dx = 0.",
            "✍️ Solve for x = 6 and evaluate optimal fare P425 and revenue P28,900."
        ],
        notes="Instructor Guidance: Show how calculus balances price elasticity against volume."
    )

    # -------------------------------------------------------------
    # SLIDE 31: Mathalino Problem 42 - Trapezoidal Gutter Video
    # -------------------------------------------------------------
    add_video_slide(
        prs,
        title="Mathalino Prob 42: Trapezoidal Gutter Capacity",
        video_path="media/videos/clips/MathalinoProblem5_TrapezoidalGutter.mp4",
        frame_path="media/frames/MathalinoProblem5_TrapezoidalGutter_frame.png",
        subtitle="14-inch metal strip bent at 45°: Maximizing hydraulic carrying capacity (Source: mathalino.com)",
        prompt_text="Base a, sides s = (14-a)/2, height h = (14-a)/(2√2). Cross-section Area A = ah + h². Setting dA/da = 0 yields optimal base width a = 14(√2 - 1)/(2√2 - 1) ≈ 3.17 inches (slants s ≈ 5.41 inches).",
        notes="Mathalino Prob 42. Source: mathalino.com/reviewer/differential-calculus/41-42-maxima-and-minima-problem-involving-a-trapezoidal-gutter. Advanced engineering civil/mechanical optimization. Exact radical algebra simplified to decimal."
    )

    # SLIDE 32: Mathalino Problem 42 - Annotation Workspace
    add_annotation_slide(
        prs,
        title="Mathalino Prob 42: Hydraulic Geometry Workspace",
        frame_path="media/frames/MathalinoProblem5_TrapezoidalGutter_frame.png",
        exercise_title="Trapezoidal Gutter (Mathalino 42)",
        instructions=[
            "Tin strip width = 14 inches. Base = a, two slant sides s = (14 - a)/2.",
            "Bending angle θ = 45°. Height h = s sin 45° = (14 - a)/(2√2).",
            "Area A = ah + h² = (14a - a²)/(2√2) + (14 - a)²/8.",
            "Differentiate: dA/da = (7 - a)/√2 + (a - 14)/4 = 0.",
            "Solve linear equation for a: a = 14(√2 - 1)/(2√2 - 1) ≈ 3.17 inches.",
            "Compute slant sides: s = (14 - 3.17)/2 ≈ 5.41 inches."
        ],
        pencil_prompts=[
            "✍️ Draw the cross-section trapezoid with base a, slants s, and height h.",
            "✍️ Write cross-sectional area A in terms of base width a.",
            "✍️ Differentiate dA/da = 0 and solve for base width a ≈ 3.17 inches."
        ],
        notes="Instructor Guidance: Demonstrate how civil and mechanical engineering channels are optimized for maximum flow."
    )

    prs.save(output_pptx)
    import shutil
    shutil.copy(output_pptx, "public/maxima_minima_lecture.pptx")
    print(f"Presentation deck successfully created at: {output_pptx} and copied to public/")

if __name__ == "__main__":
    create_deck()
