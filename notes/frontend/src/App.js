import React, {Component} from 'react';
import {Button, Container, Row, Col} from 'reactstrap';

import ListNotes from './components/ListNotes';

var notes_dummy = [
    {
        'id':1,
        'title': 'notes 1',
        'content': 'content of notes 1'
    },
    {
        'id':2,
        'title': 'notes 2',
        'content': 'content of notes 2'
    },
    {
        'id':3,
        'title': 'notes 3',
        'content': 'content of notes 3'
    },
];

class App extends Component {
    constructor(props) {
        super(props);

        this.state = {
            notes: notes_dummy,
            current_note_id: 0,
            is_creating: true,
        }

        this.handleItemClick = this.handleItemClick.bind(this);
        this.handleAddNote = this.handleAddNote.bind(this);
    }

    handleItemClick(id) {
        //console.log("id", id);
        this.setState((prevState) => {
            return { current_note_id:id, is_creating:false}
        })
    }

    handleAddNote() {
        this.setState((prevState) => {
            return { current_note_id:0, is_creating:true}
        })
    }

    render() {
        return (
            <React.Fragment>
                <Container>
                    <Row>
                        <Col xs="10">
                            <h2>Realtime Notes</h2>
                        </Col>
                        <Col xs="2">
                            <Button color="primary" onClick={this.handleAddNote}>Realtime Notes</Button>
                        </Col>
                    </Row>

                    <Row>
                        <Col xs="4">
                            <ListNotes notes={this.state.notes} handleItemClick={(id) => this.handleItemClick(id)} />
                        </Col>
                        <Col xs="8">
                            <p>Edit, update or delete</p>
                            {
                                this.state.is_creating ? "Creating" : `Editing note ${this.state.current_note_id}`
                            }
                        </Col>
                    </Row>
                </Container>
            </React.Fragment>
        );
    }
}


/*function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <h1>Hello world</h1>
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
        <Button color="danger">Hello</Button>
      </header>
    </div>
  );
}*/

export default App;
