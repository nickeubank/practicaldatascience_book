x <- 1 / 3
digits = 2
writeLines(
    format(round(x, digits), nsmall = digits),
    "my_number.txt"
)

format(round(x, 2), nsmall = 2)