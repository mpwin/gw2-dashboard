require 'rails_helper'

RSpec.describe "skins/index", type: :view do
  before(:each) do
    assign(:skins, [
      Skin.create!(
        name: "Name"
      ),
      Skin.create!(
        name: "Name"
      )
    ])
  end

  it "renders a list of skins" do
    render
    assert_select "tr>td", text: "Name".to_s, count: 2
  end
end
