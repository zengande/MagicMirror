class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = { liked: false };
    }

    render() {
        if (this.state.liked) {
            return 'You liked this.';
        }

        return (
            <a onClick={() => this.setState({ liked: true })}>link</a>
        );
    }
}

ReactDOM.render(<App />, document.querySelector('#App'));