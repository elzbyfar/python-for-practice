const reverse = (x) => {
  let str = x.toString()
  str = str.split('').reverse().join('')
  if (str.includes('-')) {
      str = str.split('-')
      return parseInt(str) * -1
  }
  if (str > Math.abs(2**31-1)) {
    return 0
}
  return parseInt(str)
}

console.log(reverse(1534236469))