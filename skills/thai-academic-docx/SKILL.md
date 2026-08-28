---
name: thai-academic-docx
description: Format or generate Microsoft Word DOCX files for Thai coursework, homework, lab reports, project reports, and casual academic reports. Use when a document is primarily Thai or follows Thai university-style academic formatting and no stricter instructor, faculty, journal, or thesis template overrides it.
---

# Thai Academic DOCX

Create clean, editable Microsoft Word documents that look like conventional Thai university coursework rather than generic themed Word documents.

This skill is an **opinionated default for casual academic work**, not a claim that every Thai university uses one universal standard.

## Priority of rules

Apply formatting in this order:

1. Explicit user instructions.
2. A supplied instructor, course, faculty, university, journal, or document template.
3. Existing formatting in a document the user asks to edit, when preserving it is part of the task.
4. This skill's Thai academic defaults.

Never override a supplied requirement merely to match this skill.

## When to use

Use this skill for DOCX work such as:

- homework and assignments
- class reports
- lab reports
- engineering reports
- project reports
- summaries and write-ups
- short research reports
- coursework containing Thai text, English technical terms, equations, tables, figures, or references

Do not automatically use these defaults for:

- formal Thai government correspondence
- theses or dissertations with an institutional template
- journal or conference submissions with author guidelines
- documents for which the user supplied a different style specification

## Visual character

Default to a plain academic appearance.

- Black/automatic text on a white page.
- No decorative horizontal rules under titles or headings.
- No colored paragraph borders, accent bars, theme lines, shading, gradients, or ornamental separators unless explicitly requested.
- Do not inherit decorative borders or colors from Word's built-in `Title`, `Subtitle`, or heading styles without checking them.
- Explicitly clear paragraph borders and shading from report title and heading styles when the source template may contain theme decoration.
- Use whitespace, font weight, size, and indentation to communicate hierarchy rather than decorative graphics.

A casual Thai coursework report should look intentionally formatted, not like a Word theme was applied automatically.

## Default page layout

Unless overridden:

- Paper size: A4
- Orientation: portrait
- Top margin: 2.54 cm
- Bottom margin: 2.54 cm
- Left margin: 2.54 cm
- Right margin: 2.54 cm
- Header/footer distance: use normal Word defaults unless content requires adjustment
- Page numbers: bottom center when page numbering is useful
- Cover page: no visible page number

Use section breaks when orientation, headers, footers, or numbering must change. Do not simulate sections with blank paragraphs.

For a genuinely wide table or figure, a temporary landscape section is allowed. Return to portrait orientation afterward unless the remaining content also requires landscape.

## Base typography

### Body text

- Font: `TH Sarabun New`
- Size: 16 pt
- Weight: regular
- Font color: automatic/black unless the user requests otherwise
- Line spacing: single
- Paragraph spacing before: 0 pt
- Paragraph spacing after: 0 pt
- First-line indent: 1.25 cm for normal prose paragraphs
- Left indent: 0 cm
- Right indent: 0 cm
- Alignment: Thai Distributed when supported and visually reasonable
- Fallback alignment: Justified

Do not use a first-line indent for headings, captions, list items, table cells, equations, block quotations, or other structures where it is inappropriate.

### Mixed Thai and English

Use `TH Sarabun New` for ordinary Thai and English prose in the same report unless a supplied template says otherwise.

Do not allow Word to silently substitute a different Latin font for English words inside Thai paragraphs when the surrounding style is meant to be uniform.

Set proofing language metadata where practical:

- Thai spans: `th-TH`
- English spans: `en-US`, unless another English locale is clearly appropriate

When Thai and English appear in the same paragraph, split spans into separate runs when useful so each script can carry the correct proofing language without changing the visual font. This helps Word avoid marking ordinary English words as misspellings merely because the paragraph is primarily Thai.

Do not disable spelling/grammar proofing globally just to hide red squiggles. Prefer correct language metadata. Acronyms, course codes, commands, identifiers, and uncommon technical terms may still be legitimately flagged by Word.

For mathematical equations, use a proper math font instead of forcing `TH Sarabun New` onto mathematical glyphs.

## Word font and language properties for Thai

Thai is handled by Microsoft Office as a complex-script language. When directly manipulating WordprocessingML, ensure complex-script font and size properties are set, not only Latin font properties.

For 16 pt body text, a robust run-font setup is conceptually equivalent to:

```xml
<w:rFonts
    w:ascii="TH Sarabun New"
    w:hAnsi="TH Sarabun New"
    w:cs="TH Sarabun New"/>
<w:sz w:val="32"/>
<w:szCs w:val="32"/>
```

`32` half-points equals 16 pt.

When manipulating XML directly, use appropriate `w:lang` metadata for Latin and complex-script text. When practical, Thai complex-script content should resolve to `th-TH`, while English prose should resolve to an English proofing locale such as `en-US`.

If the implementation library exposes only high-level font APIs, verify the generated DOCX XML or render the document to ensure Thai runs actually use the intended font.

## Heading hierarchy

Use real Word styles rather than manually bolding ordinary paragraphs and pretending they are headings.

The hierarchy must be visible through **left indentation** for numbered subsections. Do not allow heading styles to inherit the body's 1.25 cm first-line indent.

Default hierarchy:

| Style | Font | Size | Weight | Alignment | Left indent | First-line indent |
| --- | --- | ---: | --- | --- | ---: | ---: |
| Document title | TH Sarabun New | 20 pt | Bold | Center | 0 cm | 0 cm |
| Heading 1 / `1.` | TH Sarabun New | 18 pt | Bold | Left | 0 cm | 0 cm |
| Heading 2 / `1.1` | TH Sarabun New | 16 pt | Bold | Left | 1.25 cm | 0 cm |
| Heading 3 / `1.1.1` | TH Sarabun New | 16 pt | Bold | Left | 2.50 cm | 0 cm |
| Body | TH Sarabun New | 16 pt | Regular | Thai Distributed / Justified | 0 cm | 1.25 cm |

Conceptually:

```text
1. หัวข้อหลัก
    1.1 หัวข้อย่อย
        1.1.1 หัวข้อย่อยระดับถัดไป

    ย่อหน้าเนื้อหาปกติมี first-line indent 1.25 cm
```

The visible hierarchy is paragraph geometry, not literal tab characters. `Heading 2 = one 1.25 cm level` does **not** mean inserting `\t` before `1.1`.

When native multilevel numbering is used:

- anchor Heading 1 numbering at 0 cm
- anchor Heading 2 numbering at 1.25 cm
- anchor Heading 3 numbering at 2.50 cm
- use the numbering/list text position or hanging indent so wrapped heading lines align with the heading text, not underneath the number
- do not let numbering settings add an accidental extra hierarchy indent

Explicitly set both `left_indent` and `first_line_indent` for every heading style. Do not rely on inheritance from `Normal`, because body indentation can otherwise leak into headings.

Use `keep_with_next` or the Word equivalent for headings so a heading is not stranded at the bottom of a page.

Do not create more heading levels than the document needs.

For major chapters in a long report, a new-page start may be appropriate. Do not force every Heading 1 onto a new page in short homework or reports.

## Document title

Default title behavior:

- 20 pt TH Sarabun New, bold, centered
- left indent: 0 cm
- first-line indent: 0 cm
- black/automatic text
- no paragraph border
- no bottom rule
- no colored underline or accent line
- no shading
- moderate paragraph spacing rather than blank lines for separation

Avoid awkward orphaned title fragments, such as leaving a single final English word on its own line when a small size or wording adjustment can produce a more balanced title. Do not aggressively shrink a title merely to force one line.

For title/subtitle or course information, use separate paragraphs with intentional spacing. Do not create a separator line between them unless requested.

## Bold, italic, and underline

Use emphasis deliberately.

### Bold

Appropriate for:

- document titles
- headings
- table header rows
- short labels
- important terms when emphasis materially improves comprehension

Avoid:

- bolding entire body paragraphs
- repeatedly bolding arbitrary phrases
- using bold as a substitute for structural heading styles

### Italic

Appropriate for:

- scientific names
- mathematical variables when rendered as mathematics
- foreign terms when normal academic convention calls for italics
- titles of works when required by the citation style

### Underline

Avoid by default. Use only when explicitly requested or required by a template.

## Paragraph indentation and tabs

Treat indentation as paragraph geometry, not typed whitespace.

Default normal paragraph:

- first-line indent: 1.25 cm
- left indent: 0 cm
- right indent: 0 cm

Default heading indentation:

- Heading 1: left 0 cm, first-line 0 cm
- Heading 2: left 1.25 cm, first-line 0 cm
- Heading 3: left 2.50 cm, first-line 0 cm

Default tab-stop interval when a tab stop is actually needed:

- 1.25 cm

For nested non-heading structures, use approximately 0.625 to 1.25 cm additional indentation per level depending on the structure and available width. Prefer consistent increments throughout the document.

For references that require a hanging indent:

- left indent: 1.25 cm
- first-line indent: -1.25 cm

Never create visual indentation with repeated spaces.

Do not insert literal tab characters merely to simulate a first-line indent or heading level. Use paragraph/list indentation properties.

Use explicit tab stops only when tabular alignment is semantically appropriate.

## Thai line breaking and spacing

Thai text does not use spaces between every word. Let Word perform Thai line breaking.

Rules:

- Do not manually split Thai words at line endings.
- Do not insert spaces between Thai words merely to improve wrapping.
- Avoid unnatural large gaps caused by distributed alignment.
- If Thai Distributed creates visibly poor spacing, fall back to Justified or Left alignment for that paragraph.
- Keep atomic expressions together when splitting would reduce readability, such as a number with its unit, a person's name, a chemical name, or a short technical identifier.
- Use nonbreaking spaces or nonbreaking hyphens selectively when they solve a real wrapping problem.

## Lists and numbering

Use native Word numbering and bullets.

Do not manually type bullet glyphs or create alignment using spaces.

For ordinary lists, suggested indentation is:

- level 1 left indent: about 1.25 cm
- level 2 left indent: about 2.50 cm
- deeper levels: continue in consistent increments while avoiding excessive narrowing of the text column

Use hanging indentation so multi-line list items align under the item text, not under the bullet or number.

For numbered report sections such as `1.`, `1.1`, and `1.1.1`, use a real multilevel list linked to heading styles when practical, following the heading indentation rules above rather than the ordinary-list defaults.

## Tables

Use native Word tables for tabular data whenever possible.

Default rules:

- Table caption goes above the table.
- Example caption: `ตารางที่ 1 ผลการทดลอง`
- Header row: bold.
- Short header text: centered unless another alignment is more meaningful.
- Body text: normally 16 pt; 14 pt is acceptable for dense tables.
- Numeric columns: align consistently.
- Decimal values: use consistent decimal precision where the data allows it.
- Preserve readable cell padding.
- Avoid decorative borders and excessive shading.
- Repeat the header row automatically when a table spans pages.
- Avoid splitting a row across pages when doing so would harm readability.
- Use a landscape section for a table that cannot remain readable in portrait orientation.

Do not convert an editable table to an image just to preserve appearance.

If a table is reproduced or adapted from another source, include an appropriate source note and citation when the report requires attribution.

## Figures and images

Default rules:

- Center figures within the text area.
- Preserve image aspect ratio.
- Do not stretch screenshots or diagrams.
- Keep images at a readable resolution.
- Figure caption goes below the figure.
- Example caption: `รูปที่ 1 แผนผังการทำงานของระบบ`
- Keep a figure and its caption together where practical.
- Use a landscape section for a wide figure only when necessary.

If a figure comes from another source, provide source attribution when academically appropriate.

Refer to figures and tables by number:

- Prefer: `ดังแสดงในรูปที่ 3`
- Prefer: `ผลลัพธ์ในตารางที่ 2`
- Avoid: `รูปด้านบน`, `รูปด้านล่าง`, `ตารางข้างต้น`, or other position-dependent references

Use Word cross-reference fields when feasible in longer documents so references survive reordering.

## Equations and mathematics

Prefer native Word equations using OMML or Word's equation system.

Do not use equation screenshots when the expression can be represented natively.

Do not force `TH Sarabun New` onto native mathematical notation. Use `Cambria Math` or Word's appropriate native math font.

### Inline equations

Use inline mathematics for short expressions that belong grammatically inside a sentence.

Example concept:

`จากสมการ V = IR จะได้ว่า ...`

Keep the equation inline unless displaying it separately improves readability.

### Displayed equations

For important or multi-line equations:

- center the equation
- use native Word math
- add reasonable vertical spacing before and after
- keep surrounding explanatory Thai text in TH Sarabun New 16 pt

### Equation numbering

Number equations only when the document refers to them or numbering improves navigation.

Default numbering style:

- `(1)`
- `(2)`
- `(3)`

Keep the equation centered and the number aligned to the right margin using a stable layout mechanism. Do not insert repeated spaces to push the equation number to the right.

For long chapter-based reports, chapter-aware numbering such as `(3.1)` may be used when it improves clarity.

Refer to equations by number, for example `จากสมการ (2)`.

### Mathematical typography

Follow conventional mathematical typography:

- scalar variables: italic
- standard functions such as `sin`, `cos`, `log`, `ln`, `exp`: upright
- numerals: upright
- units: upright
- leave a space between a numeric value and its unit when appropriate, e.g. `5 V`, `20 Hz`, `10 m/s`

## Captions

Default caption style:

- TH Sarabun New
- 14 pt
- regular weight unless a supplied format says otherwise
- concise but descriptive

Conventions:

- table caption: above table
- figure caption: below figure

Number captions consistently throughout the document.

For long documents, use Word caption fields and cross-references when possible instead of hard-coded numbers.

## Block quotations

For a multi-line block quotation:

- do not use the normal first-line indent
- indent the block consistently from the left, and optionally the right
- preserve readable spacing before and after
- apply the required citation style

Do not simulate a block quote using many spaces.

## References and citations

Do not invent a citation style.

If the user or course specifies APA, IEEE, Vancouver, or another style, follow it.

If no citation style is specified:

- preserve any citation style already present
- otherwise use a simple, internally consistent academic format appropriate to the content
- do not fabricate publication metadata

Use hanging indents for bibliography entries when the selected citation style calls for them.

## Cover page

Add a cover page only when appropriate for the task or requested by the user.

A simple coursework cover may contain only information actually known, such as:

- report/assignment title
- course name or code
- student name
- student ID
- instructor name
- department/faculty/university
- semester or submission date

Do not invent missing personal, course, instructor, or institution details.

The cover page normally has no visible page number.

## Table of contents

Do not add a table of contents to short homework unless requested or clearly useful.

For longer reports:

- use real Word heading styles
- generate a Word TOC field from those headings
- do not manually type page numbers or dot leaders
- ensure heading levels reflect the actual document hierarchy

## Page flow and pagination

Use Word pagination controls rather than manual blank lines.

Recommended behavior:

- enable widow/orphan control for normal prose
- headings: keep with next paragraph
- avoid a heading stranded at the bottom of a page
- avoid separating a figure/table from its caption when practical
- use `page_break_before` only when a major section genuinely needs a new page

Never press Enter repeatedly to move content to a new page. Insert a real page break or section break.

## Headers, footers, and page numbers

For ordinary coursework:

- omit decorative headers unless requested
- page number default: bottom center
- hide the visible number on the cover page

If the supplied template specifies a different page-number position or numbering system, follow the template.

## Footnotes

Use real Word footnotes when footnotes are required and supported by the implementation.

Do not imitate footnotes with manually superscripted numbers plus ordinary text at the bottom of the page.

Use a smaller but readable font, generally 12 to 14 pt TH Sarabun New, unless overridden.

## Construction rules

The DOCX must remain editable and structurally sound.

Prefer:

- Word styles
- paragraph properties
- native numbering
- actual tab stops only when semantically appropriate
- real page and section breaks
- native Word tables
- native Word equations
- Word caption/cross-reference fields when practical
- proper headers and footers
- explicit style properties instead of relying on inherited theme decoration

Avoid:

- repeated spaces for alignment
- repeated blank paragraphs for vertical spacing
- literal tabs as a replacement for paragraph or heading indentation
- manually typed bullet characters when Word numbering can be used
- screenshots of equations that can be native math
- screenshots of tables that can be native tables
- hard-coded figure/table references such as "above" and "below"
- decorative title/heading rules or borders not requested by the user
- excessive manual run-by-run formatting when a reusable Word style is appropriate

## Implementation guidance for `python-docx`

When using `python-docx` or another library that does not expose every Word feature directly:

1. Define reusable paragraph and character styles early.
2. Set section size and margins explicitly.
3. Configure body first-line indentation with paragraph properties rather than inserting tabs.
4. Explicitly set heading left indents and reset heading first-line indents to zero; do not let them inherit body indentation.
5. Explicitly clear unwanted paragraph borders/shading from title and heading styles, using low-level WordprocessingML if necessary.
6. Set title and heading font color explicitly to automatic/black when a template may carry accent colors.
7. Set complex-script font (`w:cs`) and complex-script size (`w:szCs`) for Thai text when needed.
8. Set proofing language metadata for Thai and English spans where practical; split runs by script when this improves proofing behavior.
9. Use low-level WordprocessingML only for features the high-level API cannot represent correctly.
10. Use OMML for native equations when equations are required.
11. Use Word field codes for TOCs, captions, numbering, or cross-references when reliable and appropriate.
12. Do not assume a DOCX is correct merely because the generation library completed without an exception.

When creating styles from built-in Word styles, inspect inherited paragraph properties. A heading based on `Normal` can accidentally inherit `first_line_indent = 1.25 cm`; a title or heading style can also inherit a border, shading, or theme color. Reset properties explicitly when the desired value is zero/none.

## Validation

Before delivering a generated or reformatted DOCX, verify as much of the following as the environment allows.

### Structural checks

- file opens successfully as a DOCX
- A4 page size is correct
- margins are correct
- styles are actually applied
- Thai body text resolves to TH Sarabun New
- complex-script font properties are present when required
- Thai/English proofing language metadata is sensible where it was configured
- body first-line indentation is implemented as paragraph formatting
- Heading 1 has 0 cm left indent and 0 cm first-line indent
- Heading 2 has 1.25 cm left indent and 0 cm first-line indent
- Heading 3 has 2.50 cm left indent and 0 cm first-line indent
- title and heading styles have no unintended paragraph borders or shading
- no accidental repeated spaces or blank paragraphs are being used for layout
- headings use heading styles
- list numbering is native where practical
- tables remain editable
- equations remain editable/native when practical
- page and section breaks are intentional

### Visual checks

Render to PDF or inspect in Microsoft Word/LibreOffice when available and check:

- Thai glyphs are not clipped
- line spacing is comfortable
- distributed text does not create extreme gaps
- Thai/English mixed text does not unexpectedly change fonts
- ordinary English words are not broadly flagged because of incorrect proofing language
- title has no unintended horizontal line, border, accent color, or shading
- title wrapping looks intentional and does not leave an avoidable single-word orphan
- Heading 1 is visibly flush with the main text margin
- Heading 2 and Heading 3 show a clear nested hierarchy
- headings have consistent hierarchy
- no heading is stranded at the bottom of a page
- tables fit within margins
- repeated table headers work across pages
- figures preserve aspect ratio
- captions stay with their tables/figures
- equations are legible and aligned
- page numbers appear where expected
- cover page has no unwanted visible page number
- there are no unintended blank pages

If rendering reveals a conflict between a nominal rule and readability, preserve the academic intent while fixing the visual defect.

## Default style summary

Use this as the fallback profile when no stricter format is supplied:

```yaml
thai_academic_report:
  page:
    size: A4
    orientation: portrait
    margins:
      top: 2.54cm
      bottom: 2.54cm
      left: 2.54cm
      right: 2.54cm

  typography:
    prose_font: "TH Sarabun New"
    body_size: 16pt
    math_font: "Cambria Math"
    thai_language: "th-TH"
    english_language: "en-US"

  title:
    size: 20pt
    bold: true
    alignment: center
    left_indent: 0cm
    first_line_indent: 0cm
    color: black
    border: none
    shading: none

  heading_1:
    size: 18pt
    bold: true
    alignment: left
    left_indent: 0cm
    first_line_indent: 0cm
    keep_with_next: true

  heading_2:
    size: 16pt
    bold: true
    alignment: left
    left_indent: 1.25cm
    first_line_indent: 0cm
    keep_with_next: true

  heading_3:
    size: 16pt
    bold: true
    alignment: left
    left_indent: 2.50cm
    first_line_indent: 0cm
    keep_with_next: true

  body:
    size: 16pt
    alignment: thai_distributed
    fallback_alignment: justified
    left_indent: 0cm
    first_line_indent: 1.25cm
    line_spacing: 1.0
    space_before: 0pt
    space_after: 0pt
    widow_orphan_control: true

  tabs:
    default_interval: 1.25cm

  captions:
    size: 14pt
    table_position: above
    figure_position: below

  page_number:
    position: bottom_center
    hide_on_cover: true
```

## Research basis

These defaults are synthesized for practical coursework from recurring conventions in Thai academic formatting guides plus Microsoft Word/OpenXML behavior. They are deliberately simpler than thesis rules.

Useful references:

- Mae Fah Luang University thesis-formatting guidance: https://postgrads.mfu.ac.th/thesis-manual/
- Chiang Mai University academic submission guideline: https://nice.edu.cmu.ac.th/submission/guideline/
- Prince of Songkla University academic formatting guideline: https://educonf.psu.ac.th/en/en-guidelines-13/
- KMITL School of Engineering thesis template guideline: https://www.eng.kmitl.ac.th/wp-content/uploads/2024/07/20-Thesis-Template_Guideline-Rev1_28Sep20231.pdf
- Microsoft Word table-header guidance: https://support.microsoft.com/en-us/office/repeat-table-header-on-subsequent-pages-2ff677e0-3150-464a-a283-fa52794b4b41
- Microsoft Word automatic table-of-contents guidance: https://support.microsoft.com/en-us/office/insert-a-table-of-contents-882e8564-0edb-435e-84b5-1d8552ccf0c0
- Microsoft Word equations guidance: https://support.microsoft.com/en-us/office/write-an-equation-or-formula-1d01cabc-ceb1-458d-bc70-7f9737722702
- Microsoft Office complex-script language information: https://learn.microsoft.com/en-us/office/vba/api/office.msofontlanguageindex
- Open XML `RunFonts`: https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.runfonts
- Open XML language properties: https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.languages
