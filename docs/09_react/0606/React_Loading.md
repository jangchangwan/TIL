# 📖 React  Loading 구현



```javascript
import React from "react";




// 직접 실행시키지않다고 초기값으로 실행되는 함수
class App extends React.Component {
  state = {
    isLoading: true,
    movies: [],
  };
  // 5초 뒤에 화면을 보여주도록 설정
  componentDidMount(){
    setTimeout(() => {
      this.setState({ isLoading: false})
    }, 5000)
  }
  render() {
    const {isLoading} = this.state
    return (
      <div>
        {/* 삼항 연산자 사용 */}
        <h1>{isLoading ? 'Loading...': 'We are ready'}</h1>
      </div>
    );
  }
}

export default App;

```

