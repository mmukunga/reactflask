import logo from './logo.svg';
import './App.css';
import React, { useEffect, useState } from 'react';
import axios from 'axios'

function App() {
  const [myMessage, setMyMessage] = useState({})
  const [state, setState] = useState({})
  const [myMessageIds, setMyMessageIds] = useState('')
  const [myMessageName, setMyMessageName] = useState('')
  const [fileData, setFileData] = useState([])

  const options = [
    { key: 'Blåskjellsalat.txt', value: 'Blåskjellsalat.txt' },
    { key: 'Andebryst med pastinakkrem og appelsinsaus.txt', value: 'Andebryst med pastinakkrem og appelsinsaus.txt' },
    { key: 'Gulasj.txt', value: 'Gulasj.txt' },
    { key: 'Burrito med stekt kyllingfilet, ris, avokadodressing, paprika-, chili- og mangosalsa.txt', value: 'Burrito med stekt kyllingfilet, ris, avokadodressing, paprika-, chili- og mangosalsa.txt' },
  ];

  useEffect(()=>{
    axios.get('https://reactflask-smb.herokuapp.com/flask/hello').then(response => {
      console.log("SUCCESS", response);
      console.log(response);
      setMyMessage(response.data.message);
    }).catch(error => {
      console.log(error)
    });
  }, []);


  useEffect(()=>{
    const id = 100;
    axios.get(`https://reactflask-smb.herokuapp.com/flask/${id}`).then(response => {
      console.log("1.USE ID-SUCCESS: ", response);
      console.log(response);
      setMyMessageIds(response.data);
    }).catch(error => {
      console.log(error)
    });
  }, []);


  const handleChange = (e) => {
    const {name, value} = e.target
    setState({'name': name, 'value': value}); 
    console.log(`handleChange Option selected:`, value);
    console.log('handleChange The link was clicked.');
    axios.get(`https://reactflask-smb.herokuapp.com/flask/oppskriftInfo/${value}`).then(response => {
      console.log("2.handleChange SUCCESS: ", response);
      console.log(response);
      setFileData(response.data);
    }).catch(error => {
      console.log(error)
    });
  };

  const handleClick = (e) => {
    e.preventDefault();
    console.log('The link was clicked.');
    const filename = 'Gulasj.txt';
    axios.get(`https://reactflask-smb.herokuapp.com/flask/oppskriftInfo/${filename}`).then(response => {
      console.log("2.SUCCESS: ", response);
      console.log(response);
      setMyMessageName(response.data);
    }).catch(error => {
      console.log(error)
    });
  };

  console.log(fileData.Fremgangsmåte)
  console.log(fileData.Ingredienser)

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>React + Flask Tutorial</p>
        <div>{myMessage.status === 200 ? 
          <h3> Henting av meldinger fra Flask Fungerer som det skal: {myMessage.data.message} Ids {myMessageIds} Name {myMessageName} </h3>
          :
          <h3>..LOADING..</h3>}</div>
      </header>
      <h3>
      <p> xsxsx Testing - Pyton Flask Test: 
      <a href="#" onClick={handleClick}>
        Click me
      </a>
     </p>
      </h3>
      <p>
      <select onChange={e => handleChange(e)} className="SelectFile" >
        {options.map((key, value) => <option value={key}>{value}</option>)}
      </select >
      </p>
      Filer:
      <pre>
        {fileData && fileData}
      </pre>
    </div>
  );
}

export default App;
