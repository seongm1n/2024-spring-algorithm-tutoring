// 표준 입력을 읽을 수 있도록 설정.
process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputLines = []; // 입력된 줄을 저장할 변수.
let currentLine = 0; // 현재 처리 중인 줄의 인덱스 추적.

// 입력 데이터를 받아 inputLines 배열에 저장하고, main() 함수를 호출.
process.stdin.on('data', inputStdin => {
    inputLines = inputStdin.split('\n');
    main();
});

// inputLines에서 한 줄씩 읽어오는 함수.
function readLine() {
    return inputLines[currentLine++];
}

function main() {
    while (true) {
        // n, m 입력받기.
        const [n, m] = readLine().split(' ').map(Number);
        if (n === 0 && m === 0) { // 모두 0인 경우만 종료.
            break;
        }

        const calls = []; // 전화 통화 정보를 저장할 배열 초기화.
        // 전화 통화 시작 시간과 끝 시간을 저장하는 배열.
        for (let i = 0; i < n; i++) {
            const [src, dest, start, dur] = readLine().split(' ').map(Number);
            calls.push([start, start + dur]);
        }

        const results = [];
        for (let i = 0; i < m; i++) {
            // 구간의 시작 시간과 지속 시간을 입력받음.
            const [start, dur] = readLine().split(' ').map(Number);
            const end = start + dur; // 구간의 끝나는 시간 계산.
            // 구간에 포함되는 전화 통화의 수를 계산.
            const count = calls.reduce((acc, [cStart, cEnd]) => {
                // 구간에 포함되는 전화 통화의 조건을 확인, 포함되는 경우 +1 그렇지 않으면 +0
                return acc + (Math.min(end, cEnd) - Math.max(cStart, start) >= 1 ? 1 : 0);
            }, 0);
            // 구간의 결과를 results 배열에 저장.
            results.push(count);
        }

        console.log(results.join('\n'));
    }
}