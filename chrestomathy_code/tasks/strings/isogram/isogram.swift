import Foundation

func isIsogram(_ s: String) -> Bool {
    return s.count == Set(s.lowercased()).count
}

if isIsogram(CommandLine.arguments[1]) {
    print("_true_")
} else {
    print("_false_")
}