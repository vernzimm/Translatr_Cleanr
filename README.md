# Translatr_Cleanr

[Translatr](https://translatr.varunmalhotra.xyz/)

Nice little website that (Google) translates multiple languages at once. Doesn't do to well with some punctuation though. This is a little script to do several things...
  - Convert the various formatting (incomplete list, only those I have encountered)
  - Strip ending punctuation that Google occasionally invents
  - Output separate lines so we can triple-click or the like

Creates "in.txt" and "out.txt" in current working dir
  - Copy-paste translated results into "in.txt"
  - "in.txt" will be cleared after writing to "out.txt"
  - Loops every second, looking for fresh text saved into "in.txt" (will append "out.txt" for a mini-history)

Other Notes:
  - Translatr has an API... might be useful
  - Doesn't respect original text that _does_ have ending punctuation
