require 'rails_helper'

RSpec.describe "skins/new", type: :view do
  before(:each) do
    assign(:skin, Skin.new(
      name: "MyString"
    ))
  end

  it "renders new skin form" do
    render

    assert_select "form[action=?][method=?]", skins_path, "post" do

      assert_select "input[name=?]", "skin[name]"
    end
  end
end
