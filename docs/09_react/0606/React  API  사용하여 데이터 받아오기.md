# ๐ React  API  ์ฌ์ฉํ์ฌ ๋ฐ์ดํฐ ๋ฐ์์ค๊ธฐ



``` bash
npm install axios
```





``` javascript
import React from "react";
import axios from "axios";



// ์ง์  ์คํ์ํค์ง์๋ค๊ณ  ์ด๊ธฐ๊ฐ์ผ๋ก ์คํ๋๋ ํจ์
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
    // state์ ๋ฃ์ด์ฃผ๊ธฐ
    this.setState({ movies: movies})
    console.log(movies)
  }
  // 5์ด ๋ค์ ํ๋ฉด์ ๋ณด์ฌ์ฃผ๋๋ก ์ค์ 
  componentDidMount(){
    setTimeout(() => {
      this.setState({ isLoading: false})
    }, 1000);
    // ๋ฐ์ดํฐ ๋ฐ์์ค๊ธฐ
    this.getMovies();
  }
  render() {
    const {isLoading} = this.state
    return (
      <div>
        {/* ์ผํญ ์ฐ์ฐ์ ์ฌ์ฉ */}
        <h1>{isLoading ? 'Loading...': 'We are ready'}</h1>
        { this.movies }
      </div>
    );
  }
}

export default App;
```

