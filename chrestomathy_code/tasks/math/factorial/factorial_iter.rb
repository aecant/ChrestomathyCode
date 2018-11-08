def factorial (n)
    raise ArgumentError.new('Argument cannot be negative') if n < 0
    result = 1
        (2..n).each do |i|
            result *= i
        end
    result
end

n = ARGV.first.to_i
begin
    puts factorial n
rescue ArgumentError
    puts '_invalid_'
end