const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

const hegiths = [];

rl.on('line', (input) => {
  hegiths.push(parseInt(input));

  if (hegiths.length === 9) {
    rl.close();
  }
}).on('close', () => {
  // 아홈 난쟁이 중 두 명을 선택하는 모든 조합을 구합니다.
  for (let i = 0; i < 8; i++) {
    for (let j = i + 1; j < 9; j++) {
      const sum = hegiths.reduce((acc, cur) => acc + cur, 0);

      // 선택된 두 명의 키를 제외한 일곱 난쟁이의 키의 합이 100인 경우
      if (sum - hegiths[i] - hegiths[j] === 100) {
        const result = hegiths.filter((_, index) => index !== i && index !== j);
        console.log(result.sort((a, b) => a - b).join('\n'));
        return;
      }
    }
  }
})