/**
 * 주어진 시작 위치에서 8x8 크기의 체스판을 잘라내었을 때,
 * 체스판 패턴에 맞지 않는 정사각형의 개수를 계산하는 함수
 * @param {string[]} board - 보드 정보
 * @param {number} startRow - 시작 행 위치
 * @param {number} startCol - 시작 열 위치
 * @returns {number} - 체스판 패턴에 맞지 않는 정사각형의 최소 개수
 */
function countDifferences(board, startRow, startCol) {
  let count = 0;
  for (let i = 0; i < 8; i++) {
      for (let j = 0; j < 8; j++) {
          // 홀수 칸은 'W'로, 짝수 칸은 'B'로 비교
          if ((i + j) % 2 === 0) {
              if (board[startRow + i][startCol + j] !== 'W') {
                  count++;
              }
          } else {
              if (board[startRow + i][startCol + j] !== 'B') {
                  count++;
              }
          }
      }
  }
  // 패턴을 반전시켰을 때의 개수와 비교하여 최소값 반환
  return Math.min(count, 64 - count);
}

/**
* 보드에서 8x8 크기의 체스판을 잘라내었을 때,
* 체스판 패턴에 맞지 않는 정사각형의 최소 개수를 찾는 함수
* @param {number} N - 보드의 행 크기
* @param {number} M - 보드의 열 크기
* @param {string[]} board - 보드 정보
* @returns {number} - 체스판 패턴에 맞지 않는 정사각형의 최소 개수
*/
function solution(N, M, board) {
  let minDifferences = 64;
  // 모든 가능한 시작 위치에 대해 체스판을 잘라내어 최소 차이 값을 찾음
  for (let i = 0; i <= N - 8; i++) {
      for (let j = 0; j <= M - 8; j++) {
          const differences = countDifferences(board, i, j);
          minDifferences = Math.min(minDifferences, differences);
      }
  }
  return minDifferences;
}

// 입력 처리
const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let inputLines = [];
rl.on('line', (line) => {
  // 한 줄씩 입력을 받아 inputLines 배열에 저장
  inputLines.push(line);
}).on('close', () => {
  // 입력이 종료되면 실행되는 이벤트 핸들러
  const [N, M] = inputLines[0].split(' ').map(Number);
  const board = inputLines.slice(1);
  const result = solution(N, M, board);
  console.log(result);
});