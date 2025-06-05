param(
    [string] $post_name,
    [string] $post_folder = '_posts'
)

$date = Get-Date -Format "yyyy-MM-dd"
$file = "$post_folder/$date-$post_name.md"

$content = @"
---
layout: post
code: !!!PUT YOUR CODE HERE!!!
usemathjax: true
---


!!!ADD SOME TEXT HERE!!!

***
<br>

### !!!ADD YOUR 1ST HEADER HERE!!!


<br>

### !!!ADD YOUR 2ND HEADER HERE!!!


<br>
"@

$content | Out-File -Encoding ASCII -FilePath $file
Exit



