# ๐ React  ๊ธฐ์ด



## React ์์ํ๊ธฐ



``` bash
npx create-react-app ํ๋ก์ ํธ๋ช
cd ํ๋ก์ ํธ๋ช
npm start
```







## Function ์ผ๋ก ์ธ์์ ๋ฌ

``` javascript
// Movie Component๋ฅผ  ๋ค๋ฅธ ์ปดํฌ๋ํธ์ ์ฌ์ฉํ๊ธฐ
// ๋ถ๋ชจ App ์์ ๋๊ฒจ์ค ๋ฐ์ดํฐ๋ฅผ ๋ฐ๋ ๋ฐฉ๋ฒ
function Movie(props) {
  console.log(props)
  return (
    <div>
      <h1>I Like {props.fav}</h1>
    </div>
  );
}

const LikeMovies = ['๋ฅํฐ ์คํธ๋ ์ธ์ง', '๋ฒ์ฃ๋์2', 'ํด๋ฆฌํฌํฐ', '์ผ์ํฌํ์ถ']

// App Component ํจ์๋ฅผ ์ ์ํ๊ณ  ์์ ๋ฆฌํด๊ฐ์ index.js๋ก ๋๊ฒจ์ค๋ค.
function App() {
  return (
    <div className="App">
      <h1>Hello React!</h1>
      {/* 
        props๋ฅผ ์ด์ฉํ์ฌ ๋ฐ์ดํฐ๋ฅผ ๋ณด๋ด๋ ๋ฐฉ๋ฒ
        ์ฃผ์ ์์ ๋ฐ์ดํฐ๋ ๋ฌธ์์ด์ ์ ์ธํ ๋๋จธ์ง ๋ฐ์ดํฐ๋ ์ค๊ดํธ๋ก ๊ฐ์ธ์ผํ๋ค.
      */}
      {/* <Movie fav="Movie"/> */}
      {/* map์ ์ฌ์ฉํ์ฌ ๋ฆฌ์คํธ ๋๋ ๋์๋๋ฆฌ๋ฅผ ์ถ๋ ฅํ๋ ๋ฐฉ๋ฒ */}
      {LikeMovies.map(movie => (
        <Movie fav={movie}/>
      ))}
    </div>
  );
}
```



## State๋ก ๋์ ์ธ ๊ฐ ๋ถ์ฌํ๊ธฐ



``` javascript
import React from "react";

// ์ง์  ์คํ์ํค์ง์๋ค๊ณ  ์ด๊ธฐ๊ฐ์ผ๋ก ์คํ๋๋ ํจ์
class App extends React.Component {

  state = {
    cnt: 0,
  };
  // state์์ ๋ฐ๋ก ๋ฐ์ดํฐ๋ฅผ ๊ฑด๋ค ์ ์๋ค. 
  add = () => {
    console.log(this.state.cnt)
    this.setState(current =>({
        cnt: current.cnt + 1
      }))
  };
  minus = () => {
    this.setState(current =>({
      cnt: current.cnt - 1
    }))
  }

  render() {
    return (
      <div>
        <h1>I'm class component</h1>
        <h2>Count : { this.state.cnt }</h2>
        <button onClick={this.add} >add</button>
        <button onClick={this.minus}>minus</button>
      </div>
    );
  }
}

export default App;
```



## componentDidMount( ) ํจ์

์คํ์์

```
constructor( ) => render( ) => componentDidMount( )
```



![image-20220606153310781](React_0606.assets/image-20220606153310781.png)



## componentDidUpdate( ) ํจ์

```
setState()  => render() =>  componentDidUpdate()
```



![image-20220606153448990](React_0606.assets/image-20220606153448990.png)



``` javascript
import React from "react";
// ์ง์  ์คํ์ํค์ง์๋ค๊ณ  ์ด๊ธฐ๊ฐ์ผ๋ก ์คํ๋๋ ํจ์
class App extends React.Component {

  state = {
    cnt: 0,
  };
  // state์์ ๋ฐ๋ก ๋ฐ์ดํฐ๋ฅผ ๊ฑด๋ค ์ ์๋ค. 
  add = () => {
    console.log(this.state.cnt)
    this.setState(current =>({
        cnt: current.cnt + 1
      }))
  };
  minus = () => {
    this.setState(current =>({
      cnt: current.cnt - 1
    }))
  }

  componentDidMount(){
    console.log('component rendered')
  }

  componentDidUpdate(){
    console.log('component Updated')
  }

  render() {
    console.log('rendering')
    return (
      <div>
        <h1>I'm class component</h1>
        <h2>Count : { this.state.cnt }</h2>
        <button onClick={this.add} >add</button>
        <button onClick={this.minus}>minus</button>
      </div>
    );
  }
}
export default App;
```



