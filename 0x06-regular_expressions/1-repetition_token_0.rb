#!/usr/bin/env ruby
def match_school(input)
  pattern = /School/
  if input.match(pattern)
    puts "Match found!"
  else
    puts "No match."
  end
end

input = ARGV[0]
match_school(input) if input

