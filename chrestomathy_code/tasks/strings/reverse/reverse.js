function reverse(string) {
    return string.split("").reverse().join("");
}

console.log(reverse(process.argv[2]));
