numbers = [5, 10, 20, 40, 80] #numbers
total = sum(numbers) #sum

# Create and write the result to a text file
with open('result.txt', 'w') as file:
    file.write(f'The total sum is: {total}\n')
print('The result has been written to result.txt')
