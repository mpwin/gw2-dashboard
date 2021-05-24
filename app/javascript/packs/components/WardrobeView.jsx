import React from 'react';
import classNames from 'classnames';

class WardrobeView extends React.Component {
  render() {
    var views = ['collection', 'standalone'].map((view) => {
      return (
        <li className={classNames({'active': this.props.view == view})} onClick={() => this.props.selectView(view)}>{view}</li>
      );
    });

    return (
      <ul>{views}</ul>
    );
  }
}

export default WardrobeView;
