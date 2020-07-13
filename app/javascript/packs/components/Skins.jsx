import React from 'react'

class Skins extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      skins: []
    };
  }

  componentDidMount() {
    fetch('/skins.json')
      .then((response) => { return response.json() })
      .then((data)     => { this.setState({ skins: data }) });
  }

  render() {
    var skins = this.state.skins.map((skin) => {
      return (
        <li>{skin.name}</li>
      )
    })

    return(<div>{skins}</div>)
  }
}

export default Skins;
