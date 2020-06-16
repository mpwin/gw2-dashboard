require 'rails_helper'

RSpec.describe "skins/show", type: :view do
  before(:each) do
    @skin = assign(:skin, Skin.create!(
      name: "Name"
    ))
  end

  it "renders attributes in <p>" do
    render
    expect(rendered).to match(/Name/)
  end
end
