# 📖 React  API  사용하여 데이터 받아오기



``` bash
npm install axios
```





``` javascript
import React from "react";
import axios from "axios";



// 직접 실행시키지않다고 초기값으로 실행되는 함수
class App extends React.Component {
  state = {
    isLoading: true,
    movies: [],
  };

  getMovies = async () => {
    const {
      data: {
        data: {movies},
      },
    } = await axios.get('https://yts-proxy.now.sh/list_movies.json')
    // state에 넣어주기
    this.setState({ movies: movies})
    console.log(movies)
  }
  // 5초 뒤에 화면을 보여주도록 설정
  componentDidMount(){
    setTimeout(() => {
      this.setState({ isLoading: false})
    }, 1000);
    // 데이터 받아오기
    this.getMovies();
  }
  render() {
    const {isLoading} = this.state
    return (
      <div>
        {/* 삼항 연산자 사용 */}
        <h1>{isLoading ? 'Loading...': 'We are ready'}</h1>
        { this.movies }
      </div>
    );
  }
}

export default App;
```

