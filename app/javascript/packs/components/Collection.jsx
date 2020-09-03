import React from 'react';

class Collection extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    return(
      <ul class='list-group text-monospace'>
        <li class='list-group-item active'>{this.props.collection}</li>
      </ul>
    );
  }
}

export default Collection;
