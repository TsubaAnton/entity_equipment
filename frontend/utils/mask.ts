export function maskToRegex(mask) {
  const map = { N: '\\d', A: '[A-Z]', a: '[a-z]', X: '[A-Z0-9]', Z: '[-_@]' }
  return new RegExp('^' + mask.split('').map(c => map[c] || c).join('') + '$')
}

export function validateMask(sn, mask) {
  return maskToRegex(mask).test(sn)
}
