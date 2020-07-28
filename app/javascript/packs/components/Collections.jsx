import React from 'react'

class Collections extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      collections: []
    };
  }

  componentDidMount() {
    fetch('/collections.json')
      .then((response) => { return response.json() })
      .then((data)     => { this.setState({ collections: data }) });
  }

  render() {
    var collections = this.state.collections.map((collection) => {
      return (
        <li>{collection.name}</li>
      );
    });

    return(<ul>{collections}</ul>);
  }
}

export default Collections;
