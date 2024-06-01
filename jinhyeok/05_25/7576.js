const readline = require('readline'); // readline 모듈을 가져옵니다.

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const input = []; // 입력 데이터를 저장할 배열입니다.

rl.on('line', (line) => {
  input.push(line); // 각 줄을 읽어서 input 배열에 저장합니다.
}).on('close', () => {
  const [M, N] = input[0].split(' ').map(Number); // 첫 줄에서 M(가로 크기)과 N(세로 크기)을 가져옵니다.
  const box = input.slice(1).map(line => line.split(' ').map(Number)); // 다음 줄부터 상자의 상태를 이차원 배열로 변환합니다.
  
  console.log(getDaysToRipenAllTomatoes(M, N, box)); // 결과를 계산하고 출력합니다.
  
  process.exit(); // 프로세스를 종료합니다.
});

function getDaysToRipenAllTomatoes(M, N, box) {
  const directions = [
    [1, 0], // 아래쪽 방향
    [-1, 0], // 위쪽 방향
    [0, 1], // 오른쪽 방향
    [0, -1], // 왼쪽 방향
  ];
  
  const queue = []; // BFS를 위한 큐를 초기화합니다.
  let days = 0; // 최종 날짜를 저장할 변수를 초기화합니다.
  let freshTomatoes = 0; // 익지 않은 토마토의 수를 세는 변수를 초기화합니다.
  
  // 익은 토마토와 익지 않은 토마토를 큐에 추가하고, 익지 않은 토마토를 카운트합니다.
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
      if (box[i][j] === 1) { // 익은 토마토
        queue.push([i, j, 0]); // 익은 토마토의 좌표와 시작 날짜(0일)을 큐에 추가합니다.
      } else if (box[i][j] === 0) { // 익지 않은 토마토
        freshTomatoes++; // 익지 않은 토마토의 수를 증가시킵니다.
      }
    }
  }
  
  // 만약 익지 않은 토마토가 없으면 바로 0을 반환합니다.
  if (freshTomatoes === 0) return 0;

  let head = 0; // 큐의 시작점을 나타내는 변수를 초기화합니다.
  
  // BFS를 사용하여 토마토를 익히는 과정을 수행합니다.
  while (head < queue.length) {
    const [x, y, day] = queue[head++]; // 큐의 현재 좌표와 날짜를 가져옵니다.
    for (const [dx, dy] of directions) {
      const nx = x + dx; // 새로운 x 좌표
      const ny = y + dy; // 새로운 y 좌표
      
      // 새로운 좌표가 유효한 범위 내에 있고, 익지 않은 토마토가 있는 경우
      if (nx >= 0 && nx < N && ny >= 0 && ny < M && box[nx][ny] === 0) {
        box[nx][ny] = 1; // 토마토를 익게 합니다.
        queue.push([nx, ny, day + 1]); // 새로운 좌표와 날짜를 큐에 추가합니다.
        days = day + 1; // 최종 날짜를 업데이트합니다.
        freshTomatoes--; // 익지 않은 토마토의 수를 감소시킵니다.
      }
    }
  }
  
  // 모든 토마토가 익지 못한 경우 -1을 반환합니다.
  return freshTomatoes > 0 ? -1 : days;
}
