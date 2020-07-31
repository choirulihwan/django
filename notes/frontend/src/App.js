import React, {Component} from 'react';
import {Button, Container, Row, Col} from 'reactstrap';

import ListNotes from './components/ListNotes';
import { fetchNotes, fetchNote, addNote, updateNote } from './api';

/*var notes_dummy = [
    {
        'id':1,
        'title': 'learn react',
        'content': 'Learn react from zero'
    },
    {
        'id':2,
        'title': 'learn laravel',
        'content': 'Learn laravel from stretch'
    },
    {
        'id':3,
        'title': 'learn django',
        'content': 'Learn django from beginning'
    },
];*/

class App extends Component {
    constructor(props) {
        super(props);

        this.state = {
            // notes: notes_dummy,
            notes: [],
            current_note_id: 0,
            is_creating: true,
            is_fetching: true,
        }

        this.handleItemClick = this.handleItemClick.bind(this);
        this.handleAddNote = this.handleAddNote.bind(this);
        this.getData = this.getData.bind(this);
    }

    componentDidMount() {
        this.getData();
    }

    async getData() {
        let data = await fetchNotes();
        this.setState({notes: data});
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




export default App;
