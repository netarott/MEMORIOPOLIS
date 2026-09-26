# MEMORIOPOLIS English Core20 - 17 fields

## Files
- `en_core20_master_17fields.csv`: header included
- `en_core20_anki_17fields.csv`: no header, for Anki import

## Images
ConceptScene contains HTML references to the C0011-C0020 WebP files. Use the separately created package:

`MEMORIOPOLIS_ConceptImages_C0011-C0020_2026-09-26.zip`

Place its ten WebP files in Anki media before or immediately after CSV import.

## Note type and deck
- Note type: `MEMORIOPOLIS English Vocabulary`
- Deck: `MEMORIOPOLIS::English`

## Field order
1. ID
2. English
3. IPA
4. Japanese
5. PartOfSpeech
6. EnglishGrammar
7. ExampleEnglish
8. ExampleIPA
9. ExampleJapanese
10. Source
11. CourseTags
12. ExampleBreakdown
13. ExampleExplanation
14. ExamplePronunciationHint
15. UsageNote
16. ConceptContrast
17. ConceptScene

## Import
1. Copy the ten Core20 WebP files into Anki `collection.media`, or add them through Anki.
2. Import `en_core20_anki_17fields.csv` as UTF-8.
3. Select the note type and deck shown above.
4. Map all 17 columns in order.
5. Enable HTML in fields so `<img src="...">` renders.
6. Run Tools > Check Media, sync, and verify on AnkiDroid.

## Source and tag
- Source: `E0001_en`
- Tag: `memoriopolis::en::core20`
