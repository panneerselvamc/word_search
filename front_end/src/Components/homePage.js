import React, { Component } from "react";
import "../CSS_files/homePage.css";
import "semantic-ui-css/semantic.min.css";
import axios from "axios";
class App extends Component {
  state = {
    suggestedData:"",
  };
  onChangeHandler = event => {
    console.log(event.target.value);
    let data=JSON.stringify({"value":event.target.value})
    console.log(data)
    if(event.target.value!==""){
      axios.post(`http://localhost:8000/wordSearch`,data)
      .then(res => {
          console.log(res.data)
          this.setState({
            suggestedData:res.data.requiredWord
          })
          console.log(this.state.suggestedData)
      }
      )
    }
    else{
        this.setState({
            suggestedData:"",
        })
    }
  };
  render() {
    return (
      <div>
        <h2 className="title">
          <b>WORD SEARCH</b>
        </h2>
        <b>Please Enter the Word:</b>
        <div class="ui icon input loading">
          <input
            type="text"
            placeholder="Search..."
            onChange={this.onChangeHandler.bind(this)}
          />
          <i class="search icon" />
        </div>
        <br />
        <div>
        <b>Suggested Data:</b><h4 Style="display:inline;">{this.state.suggestedData}</h4>
        </div>
      </div>
    );
  }
}
// ui fluid multiple search selection dropdown
export default App;
