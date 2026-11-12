# PDF Auto-Scroller

A small Python script that automatically scrolls the window under your mouse pointer at a slow, adjustable pace. Built for reading lessons and studying from PDFs in Microsoft Edge, but it works on any webpage or document too.

## Features

- Gentle default reading speed that you can change on the fly
- Start, pause, speed up, slow down, and reverse with single-letter hotkeys
- Works with PDFs in Edge, webpages, and most other scrollable windows
- Single file, no configuration needed

## Requirements

- Windows
- Python 3.8 or newer

## Installation

```
git clone https://github.com/YOUR-USERNAME/pdf-autoscroll.git
cd pdf-autoscroll
python -m pip install -r requirements.txt
```

## Usage

1. Run the script:
   ```
   python pdf_autoscroll.py
   ```
2. Open your PDF or webpage in Edge.
3. Keep the mouse pointer over the content (scroll events go to the window under the pointer).
4. Press **S** to start scrolling.

## Hotkeys

| Key | Action                        |
|-----|-------------------------------|
| S   | Start / pause                 |
| F   | Faster                        |
| L   | Slower                        |
| R   | Reverse direction (up / down) |
| Q   | Quit                          |

While the script is running, these letters are captured by the script and will not type anywhere else. Press **Q** to quit and get them back.

## Settings

Edit the values at the top of `pdf_autoscroll.py`:

| Setting       | Default | Description                                                                              |
|---------------|---------|------------------------------------------------------------------------------------------|
| `START_SPEED` | 40      | Starting speed in pixels per second                                                      |
| `SPEED_STEP`  | 5       | How much each F / L press changes the speed                                              |
| `MIN_SPEED`   | 5       | Slowest allowed speed                                                                    |
| `MAX_SPEED`   | 300     | Fastest allowed speed                                                                    |
| `CHUNK`       | 120     | Wheel units per scroll event; lower is smoother, but some apps ignore very small values  |

## Troubleshooting

- **Nothing scrolls:** make sure the mouse pointer is over the PDF or page, and that the status line shows `SCROLLING`.
- **Hotkeys do nothing:** run your terminal as administrator, since the `keyboard` library sometimes needs it.
- **Scrolling feels choppy:** lower `CHUNK` to around 40.
- **Pointer over a video or map:** scrolling may zoom or change volume instead; move the pointer over plain text.

## License

MIT