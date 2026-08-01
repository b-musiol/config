source /usr/share/cachyos-fish-config/cachyos-config.fish
function fish_greeting
	fastfetch

	#set -l llmtext "LLMs are the asbestos of the 21st century"
	#set -l cols (tput cols)
	#set -l len (string length --visible -- "$llmtext")
	#set -l padding ( math "floor(($cols - $len) / 2)")

	#if test $padding -lt 0
	#	set padding 0
	#end

	#printf "%*s%s\n" $padding "" "$llmtext"

	echo (set_color 59000e)"                                  LLMs are the asbestos of the 21st century!"(set_color normal)
end
function fish_prompt
    # Exit status handling
    set -l st $status
    set -l st_part ""
    if test $st -ne 0
        set st_part (set_color 0080ff)"[$st]"(set_color normal)' '
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
    echo -n (set_color normal)(whoami)(set_color a28384)"@"(set_color 34a089)(hostname -s)" "
    echo -n $st_part
    echo -n (set_color 960018)$d
    echo -n (set_color 34a089)$pchar' '(set_color normal)
end
# overwrite greeting
# potentially disabling fastfetch
#function fish_greeting
#    # smth smth
#end
