# Chapter EPUBs

Build log for [md2epub.py](../md2epub.py), which converts a chapter to an
EPUB for ElevenReader TTS ingestion. Newest build first; entries are only
ever added, never rewritten, so each row records what was true at the time
it was built.

Build one chapter with:

```bash
python3 theory/chapters/md2epub.py theory/chapters/sequenced/<chapter>.md
```

Every run bumps the source version -- `ch_0_v3_2.md` becomes `ch_0_v3_3.md`,
built as `ch_0_v3_3.epub`, with the superseded EPUB removed. The `Source`
column is the version each book was built from. Pass `--no-bump` to build
in place.

Word counts are of the *spoken* text after normalization, so they include headings and the spoken bracket tokens. Listen times assume 150 wpm at 1x.

| Built | Ch | Title | Source | H1s | Words | Lines | 1x | 1.5x | 2x |
| --- | ---: | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| 2026-08-02 12:34 | 0 | Bots | ch_0_v3_2.md | 2 (First Dream: Start of the Genetic Line) | 3,995 | 241 | 27m | 18m | 13m |
| 2026-08-02 12:40 | 1 | Protocell | ch_1_v3_5.md | 1 | 10,783 | 662 | 1h 12m | 48m | 36m |
| 2026-08-02 12:39 | 2 | Prokaryote | ch_2_v3_14.md | 1 | 19,269 | 1,497 | 2h 08m | 1h 26m | 1h 04m |
| 2026-08-02 12:39 | 3 | Eukaryote | ch_3_v3_15.md | 1 | 17,019 | 653 | 1h 53m | 1h 16m | 57m |
| 2026-08-02 12:39 | 4 | Eumetazoa | ch_4_v3_14.md | 2 (Second Dream: Start of the Neuronal Line) | 14,297 | 686 | 1h 35m | 1h 04m | 48m |
| 2026-08-02 12:39 | 5 | Bilaterian | ch_5_v3_5.md | 1 | 17,637 | 673 | 1h 58m | 1h 18m | 59m |
| 2026-08-02 12:40 | 6 | Vertebrate | ch_6_v3_3.md | 1 | 12,246 | 536 | 1h 22m | 54m | 41m |
| 2026-08-02 12:39 | 7 | Mammal | ch_7_v3_3.md | 1 | 15,411 | 531 | 1h 43m | 1h 08m | 51m |
| 2026-08-02 12:39 | 8 | Primate | ch_8_v3_2.md | 2 (Third Dream: Start of the Symbolic Line) | 17,338 | 551 | 1h 56m | 1h 17m | 58m |
| 2026-08-02 12:39 | 9 | Band | ch_9_v3_3.md | 1 | 22,871 | 626 | 2h 32m | 1h 42m | 1h 16m |
| 2026-08-02 12:39 | 10 | Settlement | ch_10_v3_3.md | 1 | 19,257 | 536 | 2h 08m | 1h 26m | 1h 04m |
| 2026-08-02 12:39 | 11 | City | ch_11_v3_2.md | 1 | 19,550 | 586 | 2h 10m | 1h 27m | 1h 05m |
| 2026-08-02 12:39 | 12 | Empire | ch_12_v3_2.md | 1 | 14,859 | 444 | 1h 39m | 1h 06m | 50m |
