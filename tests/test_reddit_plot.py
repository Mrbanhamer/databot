import json
import matplotlib
matplotlib.use("Agg")  # gör att tester kan köras utan GUI

import matplotlib.pyplot as plt
from graphs.plot__graph import plot_reddit_engagement


def _write_json(path, payload):
    path.write_text(json.dumps(payload), encoding="utf-8")


def test_creates_output_file_when_save_enabled(tmp_path, monkeypatch):
    # Skapa en temporär JSON-fil
    json_file = tmp_path / "posts.json"
    out_file = tmp_path / "engagement_plot.png"

    sample_data = [
        {"upvotes": 10, "comment_count": 5},
        {"upvotes": 4, "comment_count": 2},
        {"upvotes": 0, "comment_count": 1},  # testar division-by-zero-skydd
    ]
    _write_json(json_file, sample_data)

    # Förhindra att plt.show() stoppar testet
    monkeypatch.setattr(plt, "show", lambda *args, **kwargs: None)

    plot_reddit_engagement(
        json_path=json_file,
        save_engagement_plot=True,
        output_path=out_file
    )

    assert out_file.exists()
    assert out_file.stat().st_size > 0


def test_does_not_create_file_when_save_disabled(tmp_path, monkeypatch):
    json_file = tmp_path / "posts.json"
    out_file = tmp_path / "engagement_plot.png"

    _write_json(json_file, [{"upvotes": 5, "comment_count": 1}])

    monkeypatch.setattr(plt, "show", lambda *args, **kwargs: None)

    plot_reddit_engagement(
        json_path=json_file,
        save_engagement_plot=False,
        output_path=out_file
    )

    assert not out_file.exists()
