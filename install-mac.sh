#!/bin/bash
cat<<EOF
m                                      #
#       mmm    mmmm   mmm   m mm    mmm#   mmm    m mm  m   m
#      #"  #  #" "#  #"  #  #"  #  #" "#  "   #   #"  " "m m"
#      #""""  #   #  #""""  #   #  #   #  m"""#   #      #m#
#mmmmm "#mm"  "#m"#  "#mm"  #   #  "#m##  "mm"#   #      "#
               m  #                                      m"
                ""                                      ""
mmmmm           m    #
#   "# m   m  mm#mm  # mm    mmm   m mm
#mmm#" "m m"    #    #"  #  #" "#  #"  #
#       #m#     #    #   #  #   #  #   #
#       "#      "mm  #   #  "#m#"  #   #
        m"
       ""
 mmm
m"   "  mmm   mmmmm   mmm
#   mm "   #  # # #  #"  #
#    # m"""#  # # #  #""""
"mmm" "mm"#  # # #  "#mm"

EOF
echo now installing tkinter\n
brew install tcl-tk
echo now installing Python\n
brew install python --with-tlc-tk
echo now installing pip\n
brew install pip
