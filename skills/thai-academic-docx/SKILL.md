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

Do not automatically use these defaults for formal Thai government correspondence, institution-controlled theses/dissertations, journal submissions with their own author guide, or any document for which the user supplies a different style specification.

## Visual character

Default to a plain academic appearance.

- Black/automatic text on a white page.
- No decorative horizontal rules under titles or headings.
- No colored paragraph borders, accent bars, theme lines, shading, gradients, or ornamental separators unless explicitly requested.
- Do not inherit decorative borders or colors from Word's built-in `Title`, `Subtitle`, or heading styles without checking them.
- Explicitly clear unwanted borders, shading, and theme colors from title and heading styles.
- Use whitespace, font weight, size, and indentation to communicate hierarchy.

A casual coursework report should look intentionally formatted, not like a Word theme was applied automatically.

## Default page layout

Unless overridden:

- Paper size: A4
- Orientation: portrait
- Top margin: 2.54 cm
- Bottom margin: 2.54 cm
- Left margin: 2.54 cm
- Right margin: 2.54 cm
- Header/footer distance: normal Word defaults unless content requires adjustment
- Page numbers: bottom center when page numbering is useful
- Cover page: no visible page number

Use real section breaks when orientation, headers, footers, or numbering must change. Do not simulate sections with blank paragraphs.

A genuinely wide table or figure may use a temporary landscape section. Return to portrait afterward unless the following content also requires landscape.

## Base typography

### Body text

- Font: `TH Sarabun New`
- Size: 16 pt
- Weight: regular
- Font color: automatic/black
- Line spacing: single
- Paragraph spacing before: 0 pt
- Paragraph spacing after: 0 pt
- First-line indent: 1.25 cm for normal prose
- Alignment: Thai Distributed when supported and visually reasonable
- Fallback alignment: Justified

The **left indent of body prose follows the section level that owns it**. See [Section hierarchy and prose indentation](#section-hierarchy-and-prose-indentation).

Do not use a prose first-line indent for headings, captions, list items, table cells, equations, block quotations, or other structures where it is inappropriate.

### Mixed Thai and English

Use `TH Sarabun New` for ordinary Thai and English prose in the same report unless a supplied template says otherwise.

Do not allow Word to silently substitute a different Latin font for English words inside Thai paragraphs when the surrounding style is meant to be uniform.

Set proofing-language metadata where practical:

- Thai spans: `th-TH`
- English spans: `en-US`, unless another English locale is clearly appropriate

When Thai and English appear in the same paragraph, split spans into separate runs when useful so each script can carry the correct proofing language without changing the visible font.

Do not disable spelling/grammar proofing globally merely to hide red squiggles. Acronyms, course codes, commands, identifiers, and unusual technical terms may still be legitimately flagged.

For mathematical equations, use a proper math font instead of forcing `TH Sarabun New` onto mathematical glyphs.

## Word font and language properties for Thai

Thai is handled by Microsoft Office as a complex-script language. When manipulating WordprocessingML directly, set complex-script font and size properties as well as Latin properties.

For 16 pt prose, a robust run setup is conceptually equivalent to:

```xml
<w:rFonts
    w:ascii="TH Sarabun New"
    w:hAnsi="TH Sarabun New"
    w:cs="TH Sarabun New"/>
<w:sz w:val="32"/>
<w:szCs w:val="32"/>
```

`32` half-points equals 16 pt.

When manipulating XML directly, also use appropriate `w:lang` metadata. Thai complex-script content should normally resolve to `th-TH`, while English prose should resolve to an English proofing locale such as `en-US`.

If the implementation library exposes only high-level font APIs, inspect the generated XML or render the document to confirm that Thai actually uses the intended font.

## Heading hierarchy

Use real Word heading styles rather than manually bolding ordinary paragraphs.

The hierarchy is visible partly through **left indentation**. Heading styles must not inherit the body's first-line indent.

| Style | Font | Size | Weight | Alignment | Left indent | First-line indent |
| --- | --- | ---: | --- | --- | ---: | ---: |
| Document title | TH Sarabun New | 20 pt | Bold | Center | 0 cm | 0 cm |
| Heading 1 / `1.` | TH Sarabun New | 18 pt | Bold | Left | 0 cm | 0 cm |
| Heading 2 / `1.1` | TH Sarabun New | 16 pt | Bold | Left | 1.25 cm | 0 cm |
| Heading 3 / `1.1.1` | TH Sarabun New | 16 pt | Bold | Left | 2.50 cm | 0 cm |

Conceptually:

```text
1. หัวข้อหลัก
    1.1 หัวข้อย่อย
        1.1.1 หัวข้อย่อยระดับถัดไป
```

These are paragraph/list indents, **not literal Tab characters**.

When native multilevel numbering is used:

- anchor Heading 1 numbering at 0 cm
- anchor Heading 2 numbering at 1.25 cm
- anchor Heading 3 numbering at 2.50 cm
- use list text position or hanging indentation so wrapped heading lines align with the heading text, not under the number
- do not let numbering add an accidental extra hierarchy indent

Explicitly set both `left_indent` and `first_line_indent` for every heading style. Do not rely on inheritance from `Normal`.

Use `keep_with_next` or the Word equivalent so a heading is not stranded at the bottom of a page.

Do not create more heading levels than the document needs.

## Section hierarchy and prose indentation

Body prose should visually remain inside the section that owns it.

Use the owning heading's **left indent** as the paragraph's left indent, then add the normal **1.25 cm first-line indent** on top of that.

| Paragraph belongs under | Body left indent | Body first-line indent | Absolute first-line start from margin |
| --- | ---: | ---: | ---: |
| Heading 1 / `1.` | 0 cm | 1.25 cm | 1.25 cm |
| Heading 2 / `1.1` | 1.25 cm | 1.25 cm | 2.50 cm |
| Heading 3 / `1.1.1` | 2.50 cm | 1.25 cm | 3.75 cm |

Example under a subsection:

```text
1. หัวข้อหลัก
    1.1 หัวข้อย่อย

        บรรทัดแรกของย่อหน้าเริ่มลึกเข้ามาอีกหนึ่งระดับ และเมื่อข้อความ
    ขึ้นบรรทัดใหม่ บรรทัดต่อไปกลับมาที่ระดับของหัวข้อ 1.1
```

Conceptually:

```text
1. Header
    1.1 Sub Header
        First line of body text...
    continued line of the same paragraph...
```

This is the preferred pattern for prose structurally owned by `1.1`.

Important rules:

- Do not insert one or two literal Tab characters to create this appearance.
- Use paragraph `left_indent` and `first_line_indent` properties.
- The left indent follows the **containing section depth**, not the immediately preceding paragraph by accident.
- If a paragraph is general content under Heading 1, return to Heading-1 body geometry even if a deeper Heading 2 appeared earlier.
- Lists, code blocks, quotations, tables, equations, and captions have their own indentation rules and should not blindly inherit prose indentation.
- Avoid nesting ordinary prose beyond what remains readable. If a document requires deeper heading levels, use judgment rather than continuing 1.25 cm indefinitely.

For implementation, it is reasonable to define separate body paragraph styles such as `Body H1`, `Body H2`, and `Body H3`, or to set paragraph left indentation based on the current structural section level.

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

Avoid awkward title wrapping when a small wording or size adjustment can produce a more balanced title. Do not aggressively shrink a title merely to force one line.

Use separate paragraphs with intentional spacing for title/subtitle or course information. Do not place a decorative separator line between them unless requested.

## Bold, italic, and underline

Use emphasis deliberately.

### Bold

Appropriate for:

- document titles
- headings
- table header rows
- short labels
- important terms when emphasis materially improves comprehension

Avoid bolding entire body paragraphs, repeatedly bolding arbitrary phrases, or using bold as a substitute for structural heading styles.

### Italic

Appropriate for scientific names, mathematical variables when rendered as mathematics, foreign terms when academic convention calls for italics, and titles of works when required by the citation style.

### Underline

Avoid by default. Use only when explicitly requested or required by a template.

## Paragraph indentation and tabs

Treat indentation as paragraph geometry, not typed whitespace.

Core spacing unit: **1.25 cm**.

Default heading indentation:

- Heading 1: left 0 cm, first-line 0 cm
- Heading 2: left 1.25 cm, first-line 0 cm
- Heading 3: left 2.50 cm, first-line 0 cm

Default prose indentation by section:

- body under Heading 1: left 0 cm, first-line 1.25 cm
- body under Heading 2: left 1.25 cm, first-line 1.25 cm
- body under Heading 3: left 2.50 cm, first-line 1.25 cm

Default tab-stop interval when a tab stop is actually needed: 1.25 cm.

For references that require a hanging indent:

- left indent: 1.25 cm
- first-line indent: -1.25 cm

Never create visual indentation with repeated spaces.

Do not insert literal tab characters merely to simulate a first-line indent, heading level, or body nesting. Use paragraph/list indentation properties.

Use explicit tab stops only when tabular alignment is semantically appropriate.

## Thai line breaking and spacing

Thai text does not use spaces between every word. Let Word perform Thai line breaking.

- Do not manually split Thai words at line endings.
- Do not insert spaces between Thai words merely to improve wrapping.
- Avoid unnatural large gaps caused by distributed alignment.
- If Thai Distributed produces visibly poor spacing, fall back to Justified or Left for that paragraph.
- Keep atomic expressions together when splitting would reduce readability, such as a number with its unit, a person's name, a chemical name, or a short technical identifier.
- Use nonbreaking spaces or nonbreaking hyphens selectively when they solve a real wrapping problem.

## Lists and numbering

Use native Word numbering and bullets.

Do not manually type bullet glyphs or align list content with spaces.

For ordinary lists, suggested indentation is:

- level 1 left indent: about 1.25 cm
- level 2 left indent: about 2.50 cm
- deeper levels: continue consistently while avoiding excessive narrowing

Use hanging indentation so multi-line list items align under the item text, not under the bullet or number.

For numbered report sections such as `1.`, `1.1`, and `1.1.1`, use a real multilevel list linked to heading styles when practical, following the heading rules rather than ordinary-list defaults.

## Tables

Use native Word tables whenever possible.

- Table caption goes above the table.
- Example: `ตารางที่ 1 ผลการทดลอง`
- Header row: bold.
- Short header text: centered unless another alignment is more meaningful.
- Body text: normally 16 pt; 14 pt is acceptable for dense tables.
- Numeric columns: align consistently.
- Decimal values: use consistent precision where the data allows it.
- Preserve readable cell padding.
- Avoid decorative borders and excessive shading.
- Repeat the header row automatically when a table spans pages.
- Avoid splitting a row across pages when doing so harms readability.
- Use a landscape section for a table that cannot remain readable in portrait orientation.

Do not convert an editable table to an image merely to preserve appearance.

If a table is reproduced or adapted from another source, include appropriate attribution when required.

## Figures and images

- Center figures within the text area.
- Preserve aspect ratio.
- Do not stretch screenshots or diagrams.
- Keep images at readable resolution.
- Figure caption goes below the figure.
- Example: `รูปที่ 1 แผนผังการทำงานของระบบ`
- Keep a figure and its caption together where practical.
- Use landscape only when necessary.

If a figure comes from another source, provide source attribution when academically appropriate.

Refer to figures and tables by number:

- Prefer: `ดังแสดงในรูปที่ 3`
- Prefer: `ผลลัพธ์ในตารางที่ 2`
- Avoid position-dependent references such as `รูปด้านบน`, `รูปด้านล่าง`, or `ตารางข้างต้น`

Use Word cross-reference fields when feasible in longer documents.

## Equations and mathematics

Prefer native Word equations using OMML or Word's equation system.

Do not use screenshots when an equation can be represented natively. Do not force `TH Sarabun New` onto native mathematical notation. Use `Cambria Math` or Word's appropriate native math font.

### Inline equations

Use inline mathematics for short expressions that belong grammatically inside a sentence, for example `จากสมการ V = IR จะได้ว่า ...`.

### Displayed equations

For important or multi-line equations:

- center the equation
- use native Word math
- add reasonable vertical spacing before and after
- keep surrounding Thai prose in TH Sarabun New 16 pt

### Equation numbering

Number equations only when the document refers to them or numbering improves navigation.

Default style: `(1)`, `(2)`, `(3)`.

Keep the equation centered and the number aligned to the right margin using a stable layout mechanism. Do not use repeated spaces to push the number right.

For long chapter-based reports, numbering such as `(3.1)` may be used when useful.

Refer to equations by number, for example `จากสมการ (2)`.

### Mathematical typography

- scalar variables: italic
- standard functions such as `sin`, `cos`, `log`, `ln`, `exp`: upright
- numerals: upright
- units: upright
- leave a space between a value and its unit when appropriate, e.g. `5 V`, `20 Hz`, `10 m/s`

## Captions

Default caption style:

- TH Sarabun New
- 14 pt
- regular weight unless a supplied format says otherwise
- concise but descriptive

Conventions:

- table caption: above table
- figure caption: below figure

Number captions consistently. For longer documents, use Word caption fields and cross-references when practical.

## Block quotations

For a multi-line quotation:

- do not use the normal prose first-line indent
- indent the block consistently from the left, and optionally the right
- preserve readable spacing before and after
- apply the required citation style

Do not simulate block quotations with spaces.

## References and citations

Do not invent a citation style.

If the user or course specifies APA, IEEE, Vancouver, or another style, follow it.

If no citation style is specified, preserve any style already present or otherwise use a simple, internally consistent academic format. Do not fabricate publication metadata.

Use hanging indents when the selected citation style calls for them.

## Cover page

Add a cover page only when appropriate or requested.

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

Do not add a TOC to short homework unless requested or clearly useful.

For longer reports:

- use real Word heading styles
- generate a Word TOC field from those headings
- do not manually type page numbers or dot leaders
- ensure heading levels match the actual hierarchy

## Page flow and pagination

Use Word pagination controls rather than manual blank lines.

- enable widow/orphan control for normal prose
- headings: keep with next paragraph
- avoid a heading stranded at the bottom of a page
- avoid separating a figure/table from its caption when practical
- use `page_break_before` only when a major section genuinely needs a new page

Never press Enter repeatedly to move content to a new page. Insert a real page or section break.

## Headers, footers, and page numbers

For ordinary coursework:

- omit decorative headers unless requested
- page number default: bottom center
- hide the visible number on the cover page

If the supplied template specifies a different position or numbering system, follow it.

## Footnotes

Use real Word footnotes when required and supported by the implementation.

Do not imitate footnotes with manually superscripted numbers plus ordinary text at the bottom of the page.

Use a smaller but readable font, generally 12 to 14 pt TH Sarabun New, unless overridden.

## Construction rules

The DOCX must remain editable and structurally sound.

Prefer:

- Word styles
- paragraph properties
- native multilevel numbering
- actual tab stops only when semantically appropriate
- real page and section breaks
- native Word tables
- native Word equations
- Word caption/cross-reference fields when practical
- proper headers and footers
- explicit style properties instead of relying on theme inheritance

Avoid:

- repeated spaces for alignment
- repeated blank paragraphs for vertical spacing
- literal tabs as a replacement for paragraph, heading, or nesting indentation
- manually typed bullet characters when Word numbering can be used
- screenshots of equations that can be native math
- screenshots of tables that can be native tables
- hard-coded figure/table references such as "above" and "below"
- decorative title/heading rules or borders not requested by the user
- excessive manual run-by-run formatting when a reusable style is appropriate

## Implementation guidance for `python-docx`

When using `python-docx` or another library that does not expose every Word feature directly:

1. Define reusable paragraph and character styles early.
2. Set section size and margins explicitly.
3. Configure prose indentation with paragraph properties rather than literal tabs.
4. Track structural section depth so prose under `1.1` receives `left_indent = 1.25 cm`, while prose under `1.` uses `left_indent = 0 cm`.
5. Keep `first_line_indent = 1.25 cm` for normal prose at each supported section level.
6. Consider separate styles such as `Body H1`, `Body H2`, and `Body H3` to avoid accidental indentation leakage.
7. Explicitly set heading left indents and reset heading first-line indents to zero.
8. Explicitly clear unwanted borders/shading from title and heading styles, using low-level WordprocessingML if necessary.
9. Set title and heading font color explicitly to automatic/black when a template may carry accent colors.
10. Set complex-script font (`w:cs`) and size (`w:szCs`) for Thai text when needed.
11. Set proofing-language metadata for Thai and English spans where practical; split runs by script when useful.
12. Use low-level WordprocessingML only for features the high-level API cannot represent correctly.
13. Use OMML for native equations when equations are required.
14. Use Word field codes for TOCs, captions, numbering, or cross-references when reliable and appropriate.
15. Do not assume a DOCX is correct merely because generation completed without an exception.

When creating styles from built-in Word styles, inspect inherited paragraph properties. A heading based on `Normal` can accidentally inherit a body first-line indent; a title or heading can also inherit a border, shading, or theme color. Reset properties explicitly when the desired value is zero or none.

## Validation

Before delivering a generated or reformatted DOCX, verify as much of the following as the environment allows.

### Structural checks

- file opens successfully as DOCX
- A4 page size and margins are correct
- styles are actually applied
- Thai body text resolves to TH Sarabun New
- complex-script font properties are present when required
- Thai/English proofing-language metadata is sensible where configured
- Heading 1: left 0 cm, first-line 0 cm
- Heading 2: left 1.25 cm, first-line 0 cm
- Heading 3: left 2.50 cm, first-line 0 cm
- body under Heading 1: left 0 cm, first-line 1.25 cm
- body under Heading 2: left 1.25 cm, first-line 1.25 cm
- body under Heading 3: left 2.50 cm, first-line 1.25 cm
- body paragraphs return to the correct shallower indent when section depth decreases
- title and heading styles have no unintended borders or shading
- no repeated spaces, blank paragraphs, or literal tabs are being used for layout
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
- title wrapping looks intentional
- Heading 1 is flush with the main text margin
- Heading 2 and Heading 3 show a clear nested hierarchy
- prose under a subsection is visibly owned by that subsection
- continuation lines align at the subsection's left level while the first line receives the extra 1.25 cm prose indent
- nested prose does not become so narrow that readability suffers
- no heading is stranded at the bottom of a page
- tables fit within margins and repeated headers work
- figures preserve aspect ratio
- captions stay with their tables/figures
- equations are legible and aligned
- page numbers appear where expected
- cover page has no unwanted visible page number
- there are no unintended blank pages

If rendering reveals a conflict between a nominal rule and readability, preserve the academic intent while fixing the visual defect.

## Default style summary

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
    left_indent: 0cm
    first_line_indent: 0cm
    keep_with_next: true

  heading_2:
    size: 16pt
    bold: true
    left_indent: 1.25cm
    first_line_indent: 0cm
    keep_with_next: true

  heading_3:
    size: 16pt
    bold: true
    left_indent: 2.50cm
    first_line_indent: 0cm
    keep_with_next: true

  prose:
    size: 16pt
    alignment: thai_distributed
    fallback_alignment: justified
    first_line_indent: 1.25cm
    left_indent_by_section_level:
      heading_1: 0cm
      heading_2: 1.25cm
      heading_3: 2.50cm
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
- Microsoft Word automatic TOC guidance: https://support.microsoft.com/en-us/office/insert-a-table-of-contents-882e8564-0edb-435e-84b5-1d8552ccf0c0
- Microsoft Word equations guidance: https://support.microsoft.com/en-us/office/write-an-equation-or-formula-1d01cabc-ceb1-458d-bc70-7f9737722702
- Microsoft Office complex-script language information: https://learn.microsoft.com/en-us/office/vba/api/office.msofontlanguageindex
- Open XML `RunFonts`: https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.runfonts
- Open XML language properties: https://learn.microsoft.com/en-us/dotnet/api/documentformat.openxml.wordprocessing.languages
