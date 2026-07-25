# showcolor

To display a few blocks with a hexcode colour into the terminal (useful for just seeing what the colour is), a fish-script is useful.

Paste this into fish

```
function showcolor
        for hex in $argv
            set -l clean_hex (string replace -r '^#' '' -- $hex)

            set_color -b $clean_hex
            echo -n "        "
            set_color normal

            echo -n " "
        end
        echo ""
    end
```

Then save it

```
funcsave showcolor
```

Now you can use it in any fish like
```
showcolor 749209
showcolor "#998855"
```

# Custom Prefix

To set up (in colour) that every command is prefixed by:

```
 ~/some/path$ 
```

or in case of a return value that is not 0

```
 [127] ~/some/path$ 
```

add this to `config.fish`

```
function fish_prompt
    # Exit status handling
    set -l st $status
    set -l st_part ""
    if test $st -ne 0
        set st_part (set_color red)"[$st]"(set_color normal)' '
    end

    # Current directory
    set -l d (pwd)

    # Replace $HOME with ~
    if string match -q "$HOME*" -- $d
        set d (string replace -r "^$HOME" "~" -- $d)
    end

    # Prompt character
    set -l pchar '$'
    if test (id -u) -eq 0
        set pchar '#'
    end

    # Render prompt
    echo -n " "
    echo -n $st_part
    echo -n (set_color 960018)$d
    echo -n (set_color 34a089)$pchar' '(set_color normal)
end
```

adjust colours as needed.
