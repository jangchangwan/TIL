# π React  Loading κ΅¬ν



```javascript
import React from "react";




// μ§μ  μ€νμν€μ§μλ€κ³  μ΄κΈ°κ°μΌλ‘ μ€νλλ ν¨μ
class App extends React.Component {
  state = {
    isLoading: true,
    movies: [],
  };
  // 5μ΄ λ€μ νλ©΄μ λ³΄μ¬μ£Όλλ‘ μ€μ 
  componentDidMount(){
    setTimeout(() => {
      this.setState({ isLoading: false})
    }, 5000)
  }
  render() {
    const {isLoading} = this.state
    return (
      <div>
        {/* μΌν­ μ°μ°μ μ¬μ© */}
        <h1>{isLoading ? 'Loading...': 'We are ready'}</h1>
      </div>
    );
  }
}

export default App;

```

