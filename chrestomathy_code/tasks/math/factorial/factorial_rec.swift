import Foundation

func factorial(_ n: Int) -> Int {
    if n <= 1 {return 1}
    return n * factorial(n-1)
}

let n : Int! = Int(CommandLine.arguments[1])

if n < 0 {
    print("_invalid_")
    exit(0)
}

print(factorial(n))
