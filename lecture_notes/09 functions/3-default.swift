func max(a: Int = 0, b: Int = 0) -> Int{
    if (a>b) {
        return a
    }
    else {
        return b
    }
}

print(max(a:10,b:20), max(a:10), max(a:-20))
