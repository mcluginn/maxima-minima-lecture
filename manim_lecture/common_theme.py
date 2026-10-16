from manim import *

# -------------------------------------------------------------
# GLOBAL DARK ENGINEERING THEME CONFIGURATION
# -------------------------------------------------------------
config.background_color = "#0B0F19"  # Midnight Navy
config.pixel_width = 1920
config.pixel_height = 1080
config.frame_rate = 30

# Chromatic Palette (WCAG AAA compliant on #0B0F19)
CYAN = "#38BDF8"        # Primary Function Curve / Increasing / Stability
AMBER = "#F59E0B"       # Critical Values / Tangents / Local Maxima
CORAL = "#F43F5E"       # Decreasing / Alerts / Singularities
TEXT_WHITE = "#F8FAFC"  # Pure Chalk White
MUTED_GRAY = "#94A3B8"  # Subtitles / Secondary annotations
AXES_GRAY = "#475569"   # Coordinate grids and axes
CARD_BG = "#111827"     # Dark Slate container background
BORDER_GRAY = "#1E293B" # Subtle card borders
CARD_BORDER = BORDER_GRAY
TEXT_MUTED = MUTED_GRAY
GREEN = "#10B981"
BLUE_B = "#60A5FA"
BLUE_D = "#1D4ED8"


def create_header(title_text: str, subtitle_text: str, subtitle_color: str = CYAN) -> VGroup:
    """Creates a consistent, elegant lecture header banner."""
    title = Text(title_text, font_size=32, color=TEXT_WHITE, weight=BOLD)
    subtitle = Text(subtitle_text, font_size=19, color=subtitle_color)
    header = VGroup(title, subtitle).arrange(DOWN, buff=0.12).to_edge(UP, buff=0.35)
    return header

def create_telemetry_card(width: float = 4.0, height: float = 4.8) -> RoundedRectangle:
    """Creates a standard dark slate glassmorphism container."""
    return RoundedRectangle(
        corner_radius=0.2,
        width=width,
        height=height,
        fill_color=CARD_BG,
        fill_opacity=0.92,
        stroke_color=BORDER_GRAY,
        stroke_width=1.5
    )
