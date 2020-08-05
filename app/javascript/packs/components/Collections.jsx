import React from 'react'

class Collections extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    var collections = this.props.collections.map((collection) => {
      return (
        <li>{collection.name}</li>
      );
    });

    return(<ul>{collections}</ul>);
  }
}

export default Collections;
