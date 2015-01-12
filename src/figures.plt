set terminal pngcairo  transparent enhanced font "arial,16" fontscale 1.0 size 800,600
set output "score_over_time.png"
set xlabel "iteration"
set ylabel "score"
#set logscale xy
plot 'score_over_time.dat' using 1:2 with lines lc -1 title ""


