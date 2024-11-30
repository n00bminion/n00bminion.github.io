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

"@

$content | Out-File -FilePath $file


# Add-Content -Path $file '---'
# Add-Content -Path $file 'layout: post'
# Add-Content -Path $file 'code: PUT YOUR CODE HERE'
# Add-Content -Path $file '---'




