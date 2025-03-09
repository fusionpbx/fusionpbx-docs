## Introduction

Markdown is a lightweight markup language used for formatting text. It was created by John Gruber in 2004 and has since become widely adopted, especially in the 
fields of web content creation, note-taking apps, and version control systems like Git.

Markdown allows users to write content using simple syntax that can be easily converted into HTML or other formats. This makes it an excellent choice for formatting 
text in plaintext editors, online documents, README files, and many other contexts where readable and lightweight markup is desired.

---

### Getting Started

Basic syntax to get started using markdown format.


### Headings

- **Heading 1**: `# Heading 1` or `## Heading 1`
- **Heading 2**: `## Heading 2` or `### Heading 2`
- **Heading 3**: `### Heading 3` or `#### Heading 3`

### Emphasis

- **Bold**: `**Bold text**` or `__Bold text__`
- *Italic*: `*Italic text*` or `_Italic text_`
- ***Bold Italic***: `***Bold Italic text***` or `____Bold Italic text____`
- ~~Strikethrough~~: `~~Strikethrough text~~`

### Lists

- **Unordered List**:
```
- Item 1
- Item 2
  - Nested item 2.1
```

- **Ordered List**:
```
1. Item 1
2. Item 2
   1. Nested item 2.1
```

### Links

- **Inline link**: `[Link text](https://www.example.com)`
- **Reference link**:
```
[Link text][link-id]

[link-id]: https://www.example.com
```

### Images

- **Inline image**:
```
![Alt text](image_url "Optional title")
```

### Blockquotes

```markdown
> This is a blockquote.
>
> > This is a nested blockquote.
```

### Inline code

- Surround with backticks: `` `inline code` ``

### Code blocks

- Indent each line with 4 spaces or use triple backticks ` to open code block and three to end the code block.

### Horizontal Rules

- Three or more
```
---
````

### Tables

To create tables in Markdown format, you can use pipes (`|`) for columns and dashes `-` or other characters like `=` or `_` for lines between cells. Here's how you 
can create different types of tables:

**Simple table with a single line above and below**:
```
| Header 1 | Header 2 |
|----------|----------|
| Cell 1   | Cell 2   |
| Cell 3   | Cell 4   |
```

Output:
| Header 1 | Header 2 |
|----------|----------|
| Cell 1   | Cell 2   |
| Cell 3   | Cell 4   |

---

###  Additional information

* For more advanced syntax and details, you can refer to the [John Gruber's original Markdown documentation](https://daringfireball.net/projects/markdown/syntax).
* [Markdown Tables Generator](https://www.tablesgenerator.com/markdown_tables) – An online tool to help create tables in Markdown format.
* [GitHub Flavored Markdown - Tables](https://github.github.com/gfm/#tables-extension-) – The official GitHub documentation on Markdown tables.

