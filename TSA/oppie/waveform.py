from pydub import AudioSegment
import simpleaudio as sa
from rich.progress import Progress, TimeRemainingColumn, TextColumn, ProgressColumn
from rich.text import Text
from rich.console import Console, RenderableType
from rich.table import Column
import time

# Create a console
console = Console()

class ColorChangingDotsColumn(ProgressColumn):
    """Shows progress as a row of dots that change color as progress advances."""
    
    def __init__(self, num_dots=60):
        super().__init__()
        self.num_dots = num_dots
    
    def render(self, task) -> RenderableType:
        percent_complete = task.completed / task.total if task.total > 0 else 0
        
        # Calculate how many dots should be colored (completed)
        colored_dots = int(percent_complete * self.num_dots)
        
        # Create a text with all dots, coloring the completed ones
        text = Text()
        
        # Add colored dots (completed portion)
        if colored_dots > 0:
            text.append("•" * colored_dots, style="bold yellow")
            
        # Add remaining gray dots (incomplete portion)
        remaining_dots = self.num_dots - colored_dots
        if remaining_dots > 0:
            text.append("•" * remaining_dots, style="dim")
            
        return text

    def get_table_column(self):
        return Column(ratio=1, no_wrap=True)

# === Load audio ===
song = AudioSegment.from_file("/Users/lohithsrikar/Desktop/everything/TSA/AUDIO/ytdlp-auds/Whispers in the Twilight - fullver.wav")
duration = song.duration_seconds

# === Play audio ===
play_obj = sa.play_buffer(
    song.raw_data,
    num_channels=song.channels,
    bytes_per_sample=song.sample_width,
    sample_rate=song.frame_rate
)

# === Show progress with color-changing dots using Rich ===
console.print("[bold]Whispers in the Twilight:[/bold]")

with Progress(
    TextColumn("[bold blue]{task.description}[/bold blue]"),
    ColorChangingDotsColumn(num_dots=60),
    TimeRemainingColumn(),
    console=console,
    expand=False,
    refresh_per_second=10
) as progress:
    task = progress.add_task("", total=duration)
    start = time.time()

    while not progress.finished:
        elapsed = time.time() - start
        if elapsed >= duration:
            break
        progress.update(task, completed=elapsed)
        time.sleep(0.1)

# Wait for audio to finish if it's still playing
play_obj.wait_done()
console.print("[bold green]Playback complete![/bold green]")